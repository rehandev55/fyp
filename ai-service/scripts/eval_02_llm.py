"""
Evaluation step 2 — behaviour of the three language-model agents.

Four experiments:

  A. Grounding             Each question is answered twice: once through the
                           full RAG path and once with the retrieval step
                           disabled. An independent judge model scores both for
                           faithfulness to the board textbook, curricular fit
                           and factual correctness. The difference isolates the
                           contribution of retrieval.
  B. Marking accuracy      The evaluator agent marks a gold set of student
                           answers whose correct marks were fixed in advance.
                           Reports exact agreement, mean absolute error and
                           whether the ranking of answers is preserved.
  C. Generation validity   The tester agent generates question sets that are
                           parsed mechanically for structural compliance
                           (question count, option count, answer key,
                           provenance label).
  D. Memory bounding       Prompt size across a long tutoring session, with the
                           memory manager active and with it bypassed.

Run from the ai-service directory:
    venv\\Scripts\\python.exe scripts/eval_02_llm.py
"""

import json
import re
import statistics
import sys
import time
from pathlib import Path

sys.path.insert(0, ".")

from openai import OpenAI

from memory_manager import build_messages_with_memory
from rag.retriever import _openai_client as client
from rag.retriever import format_context, retrieve
from teacher_bot import PROMPT_TEMPLATE as TEACHER_TEMPLATE
from tester_bot import evaluate_answer, generate_questions

OUT_DIR = Path("evaluation_results")
OUT_DIR.mkdir(exist_ok=True)

ANSWER_MODEL = "gpt-4o-mini"   # the model the product actually uses
JUDGE_MODEL = "gpt-4o"         # stronger, independent judge

BOARD = "federal"

# ── A. grounding test set ────────────────────────────────────────────────────
GROUNDING_QUESTIONS = [
    ("What is cell theory?", "class_11", "biology"),
    ("Explain the function of mitochondria in a cell", "class_11", "biology"),
    ("What is DNA replication?", "class_12", "biology"),
    ("Explain ionic and covalent bonding", "class_10", "chemistry"),
    ("Define oxidation and reduction", "class_12", "chemistry"),
    ("State Newton's three laws of motion", "class_9", "physics"),
    ("Explain Ohm's law", "class_10", "physics"),
    ("Define work, energy and power", "class_11", "physics"),
    ("What is differentiation in calculus?", "class_12", "mathematics"),
    ("What is an operating system?", "class_11", "computer"),
    ("Explain the difference between RAM and ROM", "class_9", "computer"),
    ("Explain active and passive voice", "class_11", "english"),
]

JUDGE_PROMPT = """You are a strict examiner for the {board} Board of Pakistan.
You are grading an AI tutor's answer written for a Class {class_level} student
studying {subject}.

Score the ANSWER on three independent criteria, each an integer from 1 to 5.

1. groundedness - is every factual claim in the ANSWER supported by the
   REFERENCE EXCERPTS? 5 = fully supported. 1 = mostly unsupported or invented.
   If the REFERENCE EXCERPTS are empty, score groundedness 1 unless the answer
   openly states it is drawing on general knowledge.
2. curriculum_fit - is the depth, vocabulary and framing right for a Class
   {class_level} board examination in this subject? 5 = exactly right.
3. correctness - is the ANSWER factually correct? 5 = no errors. 1 = seriously
   wrong.

Also report hallucinated_claims: the number of specific factual statements in
the ANSWER that are contradicted by, or absent from, the REFERENCE EXCERPTS.

Reply with JSON only, no prose, in exactly this shape:
{{"groundedness": n, "curriculum_fit": n, "correctness": n,
  "hallucinated_claims": n, "note": "one short sentence"}}

QUESTION:
{question}

REFERENCE EXCERPTS:
{context}

ANSWER:
{answer}
"""


def judge(question, context, answer, class_level, subject) -> dict:
    prompt = JUDGE_PROMPT.format(
        board=BOARD, class_level=class_level, subject=subject,
        question=question, context=context or "(none)", answer=answer,
    )
    response = client.chat.completions.create(
        model=JUDGE_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=250,
        response_format={"type": "json_object"},
    )
    raw = response.choices[0].message.content
    usage = response.usage
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        parsed = {"groundedness": 0, "curriculum_fit": 0, "correctness": 0,
                  "hallucinated_claims": -1, "note": "unparsable judge reply"}
    parsed["_judge_tokens"] = usage.prompt_tokens + usage.completion_tokens
    return parsed


def answer_with_rag(question, class_level, subject):
    """The production path: retrieve, then generate."""
    t0 = time.perf_counter()
    chunks = retrieve(question, BOARD, class_level, subject, top_k=5)
    context = format_context(chunks)
    system_prompt = TEACHER_TEMPLATE.format(
        board=BOARD, class_level=class_level, subject=subject,
        context=context, question=question,
    )
    messages, _ = build_messages_with_memory(
        system_prompt=system_prompt, chat_history=[],
        question=question, existing_summary="",
    )
    response = client.chat.completions.create(
        model=ANSWER_MODEL, messages=messages,
        temperature=0.3, max_tokens=1000,
    )
    return {
        "answer": response.choices[0].message.content,
        "context": context,
        "n_chunks": len(chunks),
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "latency_s": round(time.perf_counter() - t0, 2),
    }


def answer_without_rag(question, class_level, subject):
    """Control: identical prompt, retrieval disabled."""
    t0 = time.perf_counter()
    system_prompt = TEACHER_TEMPLATE.format(
        board=BOARD, class_level=class_level, subject=subject,
        context="No relevant content found.", question=question,
    )
    response = client.chat.completions.create(
        model=ANSWER_MODEL,
        messages=[{"role": "system", "content": system_prompt},
                  {"role": "user", "content": question}],
        temperature=0.3, max_tokens=1000,
    )
    return {
        "answer": response.choices[0].message.content,
        "context": "",
        "n_chunks": 0,
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "latency_s": round(time.perf_counter() - t0, 2),
    }


def experiment_a() -> dict:
    print("\n[A] Grounding: RAG path versus retrieval-disabled control")
    rows = []
    for question, class_level, subject in GROUNDING_QUESTIONS:
        rag = answer_with_rag(question, class_level, subject)
        base = answer_without_rag(question, class_level, subject)

        # Both answers are judged against the SAME retrieved excerpts, so the
        # control is measured on whether it happens to agree with the board
        # textbook, not on whether it sounds plausible.
        j_rag = judge(question, rag["context"], rag["answer"],
                      class_level, subject)
        j_base = judge(question, rag["context"], base["answer"],
                       class_level, subject)

        rows.append({
            "question": question, "class": class_level, "subject": subject,
            "rag": {**{k: v for k, v in rag.items() if k != "context"},
                    "judge": j_rag},
            "control": {**{k: v for k, v in base.items() if k != "context"},
                        "judge": j_base},
        })
        print(f"  {subject:12} {class_level:9} "
              f"RAG g={j_rag['groundedness']} c={j_rag['correctness']} "
              f"h={j_rag['hallucinated_claims']} | "
              f"CTRL g={j_base['groundedness']} c={j_base['correctness']} "
              f"h={j_base['hallucinated_claims']}  {question[:34]}")

    def agg(side, key):
        vals = [r[side]["judge"][key] for r in rows]
        return round(statistics.mean(vals), 3)

    summary = {
        "n": len(rows),
        "rag": {
            "groundedness": agg("rag", "groundedness"),
            "curriculum_fit": agg("rag", "curriculum_fit"),
            "correctness": agg("rag", "correctness"),
            "hallucinated_claims": agg("rag", "hallucinated_claims"),
            "mean_prompt_tokens": round(statistics.mean(
                [r["rag"]["prompt_tokens"] for r in rows]), 1),
            "mean_latency_s": round(statistics.mean(
                [r["rag"]["latency_s"] for r in rows]), 2),
        },
        "control": {
            "groundedness": agg("control", "groundedness"),
            "curriculum_fit": agg("control", "curriculum_fit"),
            "correctness": agg("control", "correctness"),
            "hallucinated_claims": agg("control", "hallucinated_claims"),
            "mean_prompt_tokens": round(statistics.mean(
                [r["control"]["prompt_tokens"] for r in rows]), 1),
            "mean_latency_s": round(statistics.mean(
                [r["control"]["latency_s"] for r in rows]), 2),
        },
    }
    return {"summary": summary, "rows": rows}


# ── B. marking accuracy gold set ─────────────────────────────────────────────
# expected marks agreed against the board marking scheme before the run
GOLD_ANSWERS = [
    ("What is cell theory?",
     "Cell theory states that all living organisms are made of cells, the cell "
     "is the basic structural and functional unit of life, and all cells arise "
     "from pre-existing cells.",
     "short", "class_11", "biology", 3),
    ("What is cell theory?",
     "Cell theory says living things are made of cells.",
     "short", "class_11", "biology", 1),
    ("What is cell theory?",
     "Cell theory explains how planets orbit the sun.",
     "short", "class_11", "biology", 0),
    ("State Newton's second law of motion.",
     "Newton's second law states that the acceleration of a body is directly "
     "proportional to the net force acting on it and inversely proportional to "
     "its mass, F = ma.",
     "short", "class_9", "physics", 3),
    ("State Newton's second law of motion.",
     "Force equals mass times acceleration.",
     "short", "class_9", "physics", 2),
    ("State Newton's second law of motion.",
     "Every action has an equal and opposite reaction.",
     "short", "class_9", "physics", 0),
    ("Define oxidation.",
     "Oxidation is the loss of electrons by an atom, ion or molecule, which "
     "increases its oxidation number.",
     "short", "class_12", "chemistry", 3),
    ("Define oxidation.",
     "Oxidation is when something gains electrons.",
     "short", "class_12", "chemistry", 0),
    ("What does RAM stand for?",
     "Random Access Memory", "mcq", "class_9", "computer", 1),
    ("What does RAM stand for?",
     "Read Access Machine", "mcq", "class_9", "computer", 0),
    ("Explain Ohm's law and its mathematical form.",
     "Ohm's law states that the current passing through a conductor is "
     "directly proportional to the potential difference across it, provided "
     "the physical conditions such as temperature remain constant. It is "
     "written as V = IR, where V is the potential difference in volts, I is "
     "the current in amperes and R is the resistance in ohms. The law applies "
     "to ohmic conductors, and a graph of V against I for such a conductor is "
     "a straight line through the origin whose slope gives the resistance.",
     "long", "class_10", "physics", 8),
    ("Explain Ohm's law and its mathematical form.",
     "Ohm's law is V = IR. Current is related to voltage.",
     "long", "class_10", "physics", 3),
    ("Explain Ohm's law and its mathematical form.",
     "Ohm's law describes how light bends when passing through a prism.",
     "long", "class_10", "physics", 0),
    ("Define work, energy and power.",
     "Work is done when a force moves a body through a distance in the "
     "direction of the force, W = F d cos(theta), measured in joules. Energy "
     "is the capacity of a body to do work and is also measured in joules. "
     "Power is the rate of doing work, P = W / t, and is measured in watts.",
     "long", "class_11", "physics", 8),
    ("Define work, energy and power.",
     "Work is force. Energy is power. Power is work.",
     "long", "class_11", "physics", 1),
]


def experiment_b() -> dict:
    print("\n[B] Marking accuracy of the evaluator agent")
    rows = []
    for question, answer, qtype, class_level, subject, expected in GOLD_ANSWERS:
        t0 = time.perf_counter()
        result = evaluate_answer(
            question=question, student_answer=answer, board=BOARD,
            class_level=class_level, subject=subject, question_type=qtype,
        )
        rows.append({
            "question": question, "answer": answer, "type": qtype,
            "class": class_level, "subject": subject,
            "expected": expected, "awarded": result["score"],
            "error": result["score"] - expected,
            "feedback": result["feedback"],
            "latency_s": round(time.perf_counter() - t0, 2),
        })
        mark = "OK " if result["score"] == expected else "DIFF"
        print(f"  [{mark}] {qtype:5} expected={expected} awarded="
              f"{result['score']} {subject:10} {answer[:40]}")

    errors = [abs(r["error"]) for r in rows]
    exact = sum(1 for r in rows if r["error"] == 0)
    within1 = sum(1 for r in rows if abs(r["error"]) <= 1)

    # normalised error: absolute error over the maximum mark for that type
    maxima = {"mcq": 1, "short": 3, "long": 8}
    norm = [abs(r["error"]) / maxima[r["type"]] for r in rows]

    by_type = {}
    for qtype in ("mcq", "short", "long"):
        sub = [r for r in rows if r["type"] == qtype]
        if sub:
            by_type[qtype] = {
                "n": len(sub),
                "exact": sum(1 for r in sub if r["error"] == 0),
                "mae": round(statistics.mean(
                    [abs(r["error"]) for r in sub]), 3),
            }

    summary = {
        "n": len(rows),
        "exact_agreement": round(exact / len(rows), 4),
        "within_1_mark": round(within1 / len(rows), 4),
        "mae_marks": round(statistics.mean(errors), 3),
        "normalised_mae": round(statistics.mean(norm), 4),
        "mean_latency_s": round(statistics.mean(
            [r["latency_s"] for r in rows]), 2),
        "by_type": by_type,
    }
    return {"summary": summary, "rows": rows}


# ── C. generation structural validity ────────────────────────────────────────
GENERATION_TASKS = [
    ("cell theory", "class_11", "biology", "mcq", 5),
    ("chemical bonding", "class_10", "chemistry", "mcq", 5),
    ("laws of motion", "class_9", "physics", "mcq", 5),
    ("matrices", "class_10", "mathematics", "short", 3),
    ("operating systems", "class_11", "computer", "short", 3),
    ("electromagnetic induction", "class_12", "physics", "long", 2),
]

LABEL_RE = re.compile(r"(⭐|~|★)\s*(Past Paper|Similar|New)?", re.IGNORECASE)
QNUM_RE = re.compile(r"^\s*Q\s*\[?(\d+)\]?[.)]", re.MULTILINE)
OPTION_RE = re.compile(r"^\s*([ABCD])\)", re.MULTILINE)
CORRECT_RE = re.compile(r"^\s*Correct\s*:\s*([ABCD])", re.MULTILINE | re.IGNORECASE)


def experiment_c() -> dict:
    print("\n[C] Structural validity of generated question sets")
    rows = []
    for topic, class_level, subject, qtype, n in GENERATION_TASKS:
        t0 = time.perf_counter()
        raw = generate_questions(
            topic=topic, board=BOARD, class_level=class_level,
            subject=subject, question_type=qtype, num_questions=n,
        )
        latency = round(time.perf_counter() - t0, 2)

        found_q = len(QNUM_RE.findall(raw))
        labels = len(LABEL_RE.findall(raw))
        options = len(OPTION_RE.findall(raw))
        keys = len(CORRECT_RE.findall(raw))

        checks = {
            "question_count_correct": found_q == n,
            "every_question_labelled": labels >= found_q > 0,
        }
        if qtype == "mcq":
            checks["four_options_each"] = options == 4 * n
            checks["answer_key_present"] = keys == n
        else:
            checks["answer_section_present"] = raw.lower().count("answer:") >= n

        passed = sum(1 for v in checks.values() if v)
        rows.append({
            "topic": topic, "class": class_level, "subject": subject,
            "type": qtype, "requested": n, "found": found_q,
            "labels": labels, "options": options, "keys": keys,
            "checks": checks, "checks_passed": passed,
            "checks_total": len(checks), "latency_s": latency,
            "raw": raw,
        })
        print(f"  {qtype:5} {subject:12} requested={n} found={found_q} "
              f"checks {passed}/{len(checks)}  ({latency}s)")

    total_checks = sum(r["checks_total"] for r in rows)
    total_passed = sum(r["checks_passed"] for r in rows)
    summary = {
        "n_sets": len(rows),
        "checks_passed": total_passed,
        "checks_total": total_checks,
        "structural_pass_rate": round(total_passed / total_checks, 4),
        "sets_fully_valid": sum(
            1 for r in rows if r["checks_passed"] == r["checks_total"]),
        "mean_latency_s": round(statistics.mean(
            [r["latency_s"] for r in rows]), 2),
    }
    return {"summary": summary, "rows": rows}


# ── D. memory bounding ───────────────────────────────────────────────────────
SESSION_TURNS = [
    "What is cell theory?",
    "Who proposed it?",
    "What is the structure of a plant cell?",
    "How is it different from an animal cell?",
    "What does the mitochondrion do?",
    "Why is it called the powerhouse of the cell?",
    "What is the role of the nucleus?",
    "Explain what chromatin is.",
    "How does the cell membrane control what enters the cell?",
    "Summarise everything we discussed about the cell.",
]


def count_tokens(messages: list) -> int:
    """Approximate prompt size: 4 characters per token is close enough for
    gpt-4o-mini and avoids a tiktoken dependency in the evaluation path."""
    chars = sum(len(m["content"]) for m in messages)
    return chars // 4


def experiment_d() -> dict:
    print("\n[D] Prompt growth across a 10-turn session")
    class_level, subject = "class_11", "biology"
    system_prompt = TEACHER_TEMPLATE.format(
        board=BOARD, class_level=class_level, subject=subject,
        context="(fixed context held constant for this experiment)",
        question="",
    )

    history, summary = [], ""
    managed, naive = [], []
    naive_history = []

    for i, question in enumerate(SESSION_TURNS, start=1):
        messages, summary = build_messages_with_memory(
            system_prompt=system_prompt, chat_history=history,
            question=question, existing_summary=summary,
        )
        managed.append(count_tokens(messages))

        naive_messages = ([{"role": "system", "content": system_prompt}]
                          + naive_history
                          + [{"role": "user", "content": question}])
        naive.append(count_tokens(naive_messages))

        # a representative assistant reply so the history grows realistically
        reply = ("A board-style explanation of about eighty words. " * 8)
        history += [{"role": "user", "content": question},
                    {"role": "assistant", "content": reply}]
        naive_history += [{"role": "user", "content": question},
                          {"role": "assistant", "content": reply}]

        print(f"  turn {i:2}: managed={managed[-1]:6} tokens   "
              f"naive={naive[-1]:6} tokens")

    summary_stats = {
        "turns": len(SESSION_TURNS),
        "managed_tokens": managed,
        "naive_tokens": naive,
        "managed_final": managed[-1],
        "naive_final": naive[-1],
        "growth_managed": managed[-1] - managed[0],
        "growth_naive": naive[-1] - naive[0],
        "tokens_saved_final_turn": naive[-1] - managed[-1],
        "reduction_final_turn": round(1 - managed[-1] / naive[-1], 4),
        "final_summary": summary,
    }
    return summary_stats


def main() -> None:
    print("=" * 62)
    print("LANGUAGE-MODEL AGENT EVALUATION")
    print(f"answer model: {ANSWER_MODEL}   judge model: {JUDGE_MODEL}")
    print("=" * 62)

    results = {
        "config": {"answer_model": ANSWER_MODEL, "judge_model": JUDGE_MODEL,
                   "board": BOARD},
        "a_grounding": experiment_a(),
        "b_marking": experiment_b(),
        "c_generation": experiment_c(),
        "d_memory": experiment_d(),
    }

    print("\n" + "=" * 62)
    print("SUMMARY")
    print("=" * 62)
    a = results["a_grounding"]["summary"]
    print(f"  grounding   RAG  g={a['rag']['groundedness']} "
          f"fit={a['rag']['curriculum_fit']} "
          f"corr={a['rag']['correctness']} "
          f"halluc={a['rag']['hallucinated_claims']}")
    print(f"              CTRL g={a['control']['groundedness']} "
          f"fit={a['control']['curriculum_fit']} "
          f"corr={a['control']['correctness']} "
          f"halluc={a['control']['hallucinated_claims']}")
    b = results["b_marking"]["summary"]
    print(f"  marking     exact={b['exact_agreement']} "
          f"within1={b['within_1_mark']} MAE={b['mae_marks']}")
    c = results["c_generation"]["summary"]
    print(f"  generation  pass_rate={c['structural_pass_rate']} "
          f"fully_valid={c['sets_fully_valid']}/{c['n_sets']}")
    d = results["d_memory"]
    print(f"  memory      final managed={d['managed_final']} "
          f"naive={d['naive_final']} "
          f"reduction={d['reduction_final_turn']}")

    out = OUT_DIR / "llm_eval.json"
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False),
                   encoding="utf-8")
    print(f"\nWritten: {out}")


if __name__ == "__main__":
    main()
