"""
Generate every chart used in the report.

Diagrams (architecture, data flow, entity relationship, the three SRS analysis
models and so on) are static image files already present in thesis/figures.
This script produces only the charts that are derived from data: the
requirement survey, the retrieval and language-model evaluations, and the
repository activity record.

    python thesis/build_figures.py
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import survey_data as sd
from chart_kit import (bar_chart, grouped_bar_chart, hbar_chart, line_chart,
                       pie_chart)

FIG = os.path.join(HERE, "figures")
EVAL = os.path.join(ROOT, "ai-service", "evaluation_results")


def split(pairs):
    return [p[0] for p in pairs], [p[1] for p in pairs]


# ── survey ───────────────────────────────────────────────────────────────────
def survey_figures():
    made = []
    labels, values = split(sd.CLASS_DISTRIBUTION)
    made.append(pie_chart(
        f"{FIG}/fig_survey_class.png",
        "Class of respondents", labels, values,
        note=f"n = {sd.N}"))

    labels, values = split(sd.STUDY_LOCATION)
    made.append(pie_chart(
        f"{FIG}/fig_survey_location.png",
        "Where respondents study most", labels, values, note=f"n = {sd.N}"))

    labels, values = split(sd.WHEN_STUCK)
    made.append(hbar_chart(
        f"{FIG}/fig_survey_stuck.png",
        "What students do when they do not understand a topic",
        labels, values, label_w=230,
        note=f"n = {sd.WHEN_STUCK_N}; more than one answer allowed"))

    labels, values = split(sd.online_tool_groups())
    made.append(pie_chart(
        f"{FIG}/fig_survey_tools.png",
        "Use of online study tools", labels, values, note=f"n = {sd.N}"))

    themes, reported = sd.chatgpt_problem_themes()
    labels, values = split(themes)
    made.append(hbar_chart(
        f"{FIG}/fig_survey_chatgpt_problems.png",
        "Problems reported with general-purpose assistants",
        labels, values, label_w=300,
        note=f"{reported} of 45 respondents reported a problem; "
             f"responses may carry more than one theme"))

    labels, values = split(sd.NEEDS_HELP_WITH)
    made.append(pie_chart(
        f"{FIG}/fig_survey_help.png",
        "What students need more help with", labels, values,
        note=f"n = {sd.N}"))

    labels, values = split(sd.BOARD_SYLLABUS_APP)
    made.append(pie_chart(
        f"{FIG}/fig_survey_boardapp.png",
        "Value of an application tied to the board syllabus",
        labels, values, note=f"n = {sd.N}"))

    labels, values = split(sd.CHATBOT_TEST)
    made.append(pie_chart(
        f"{FIG}/fig_survey_chatbot_test.png",
        "Value of a chatbot that tests, marks and explains",
        labels, values, note=f"n = {sd.N}"))

    labels, values = split(sd.DOWNLOADS_MATERIAL)
    made.append(pie_chart(
        f"{FIG}/fig_survey_downloads.png",
        "Ease of finding past papers and textbooks online",
        labels, values, note=f"n = {sd.N}"))

    labels, values = split(sd.BOARD_VS_ONLINE)
    made.append(pie_chart(
        f"{FIG}/fig_survey_boardvsonline.png",
        "Perceived mismatch between board content and online material",
        labels, values, note=f"n = {sd.N}"))

    labels, values = split(sd.feature_themes())
    made.append(hbar_chart(
        f"{FIG}/fig_survey_features.png",
        "Features students asked for in a learning application",
        labels, values, label_w=320,
        note=f"n = {sd.N}; free text coded into themes, "
             f"more than one theme per response"))

    labels, values = split(sd.difficulty_themes())
    made.append(hbar_chart(
        f"{FIG}/fig_survey_difficulty.png",
        "Biggest difficulty reported while studying",
        labels, values, label_w=280,
        note="n = 46; free text coded into themes"))
    return made


# ── evaluation ───────────────────────────────────────────────────────────────
def evaluation_figures():
    made = []
    inv_path = os.path.join(EVAL, "index_inventory.json")
    ret_path = os.path.join(EVAL, "retrieval_eval.json")
    llm_path = os.path.join(EVAL, "llm_eval.json")

    if os.path.exists(inv_path):
        inv = json.load(open(inv_path, encoding="utf-8"))
        order = ["class_9", "class_10", "class_11", "class_12"]
        labels = ["Class 9", "Class 10", "Class 11", "Class 12"]
        values = [inv["by_class"].get(k, 0) for k in order]
        made.append(bar_chart(
            f"{FIG}/fig_eval_corpus_class.png",
            "Indexed chunks by class", labels, values,
            ylabel="chunks", colour=(37, 99, 235)))

        labels, values = split([(t["type"].replace("_", " ").title(),
                                 t["chunks"]) for t in inv["doc_types"]])
        made.append(bar_chart(
            f"{FIG}/fig_eval_corpus_type.png",
            "Indexed chunks by document type", labels, values,
            ylabel="chunks"))

        subj = sorted(inv["by_subject"].items(), key=lambda kv: -kv[1])
        labels = [s.title() for s, _ in subj]
        values = [v for _, v in subj]
        made.append(hbar_chart(
            f"{FIG}/fig_eval_corpus_subject.png",
            "Indexed chunks by subject", labels, values, label_w=160,
            note=f"total {inv['stats']['total_vector_count']:,} vectors"))

    if os.path.exists(ret_path):
        ret = json.load(open(ret_path, encoding="utf-8"))
        by_subject = {}
        for row in ret["per_query"]:
            by_subject.setdefault(row["subject"], []).append(row["top1_score"])
        items = sorted(((k, sum(v) / len(v)) for k, v in by_subject.items()),
                       key=lambda kv: -kv[1])
        labels = [k.title() for k, _ in items]
        values = [round(v, 3) for _, v in items]
        made.append(bar_chart(
            f"{FIG}/fig_eval_retrieval_scores.png",
            "Mean top-1 similarity of retrieved chunks, by subject",
            labels, values, ylabel="cosine similarity",
            value_fmt="{:.3f}", colour=(5, 150, 105)))

        buckets = [0, 0, 0, 0]
        for row in ret["per_query"]:
            s = row["top1_score"]
            idx = 0 if s < 0.35 else 1 if s < 0.45 else 2 if s < 0.55 else 3
            buckets[idx] += 1
        made.append(bar_chart(
            f"{FIG}/fig_eval_score_distribution.png",
            "Distribution of top-1 similarity across 30 test queries",
            ["below 0.35", "0.35 - 0.45", "0.45 - 0.55", "0.55 and above"],
            buckets, ylabel="queries", colour=(124, 58, 237)))

    if os.path.exists(llm_path):
        llm = json.load(open(llm_path, encoding="utf-8"))

        a = llm["a_grounding"]["summary"]
        made.append(grouped_bar_chart(
            f"{FIG}/fig_eval_grounding.png",
            "Judged answer quality: retrieval enabled versus disabled",
            ["Groundedness", "Curriculum fit", "Correctness"],
            [("With retrieval (RAG)", [a["rag"]["groundedness"],
                                       a["rag"]["curriculum_fit"],
                                       a["rag"]["correctness"]]),
             ("Retrieval disabled", [a["control"]["groundedness"],
                                     a["control"]["curriculum_fit"],
                                     a["control"]["correctness"]])],
            ylabel="judge score (1 - 5)", value_fmt="{:.2f}",
            note=f"n = {a['n']} questions, judged by an independent model"))

        made.append(bar_chart(
            f"{FIG}/fig_eval_hallucination.png",
            "Mean unsupported claims per answer",
            ["With retrieval (RAG)", "Retrieval disabled"],
            [a["rag"]["hallucinated_claims"],
             a["control"]["hallucinated_claims"]],
            ylabel="claims per answer", value_fmt="{:.2f}")),

        b = llm["b_marking"]
        rows = b["rows"]
        made.append(grouped_bar_chart(
            f"{FIG}/fig_eval_marking.png",
            "Evaluator agent: expected mark against awarded mark",
            [f"{r['type'].upper()} {i + 1}" for i, r in enumerate(rows)],
            [("Expected", [r["expected"] for r in rows]),
             ("Awarded", [r["awarded"] for r in rows])],
            ylabel="marks", value_fmt="{:.0f}", w=1000,
            note=f"exact agreement {b['summary']['exact_agreement'] * 100:.1f}%"
                 f", all marks within one of the expected value"))

        d = llm["d_memory"]
        turns = list(range(1, d["turns"] + 1))
        made.append(line_chart(
            f"{FIG}/fig_eval_memory.png",
            "Prompt size across a ten-turn tutoring session",
            turns,
            [("With memory manager", d["managed_tokens"]),
             ("Full history resent", d["naive_tokens"])],
            ylabel="prompt tokens", xlabel="conversation turn"))

    usage = os.path.join(ROOT, "ai-service", "data", "token_usage.jsonl")
    if os.path.exists(usage):
        by_endpoint = {}
        with open(usage, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                slot = by_endpoint.setdefault(rec["endpoint"],
                                              {"calls": 0, "tokens": 0})
                slot["calls"] += 1
                slot["tokens"] += rec["total_tokens"]
        items = sorted(by_endpoint.items(), key=lambda kv: -kv[1]["tokens"])
        labels = [k.replace("_", " ") for k, _ in items]
        values = [round(v["tokens"] / v["calls"]) for _, v in items]
        made.append(bar_chart(
            f"{FIG}/fig_eval_tokens.png",
            "Mean tokens per call, by endpoint", labels, values,
            ylabel="tokens", colour=(217, 119, 6)))
    return made


# ── repository ───────────────────────────────────────────────────────────────
REPO_COMMITS_BY_MONTH = [("Apr 2026", 27), ("May 2026", 49),
                         ("Jun 2026", 9), ("Sep 2026", 4)]

CODEBASE = [("TypeScript and React\n(hand written)", 10640),
            ("TypeScript\n(generated routes)", 8795),
            ("PHP application", 4252),
            ("Python AI service", 2868),
            ("PHP tests", 753)]


def repository_figures():
    made = []
    labels, values = split(REPO_COMMITS_BY_MONTH)
    made.append(bar_chart(
        f"{FIG}/fig_repo_commits.png",
        "Commits to the project repository by month",
        labels, values, ylabel="commits", colour=(37, 99, 235)))

    labels, values = split(CODEBASE)
    made.append(hbar_chart(
        f"{FIG}/fig_repo_codebase.png",
        "Size of the delivered codebase",
        [l.replace("\n", " ") for l in labels], values, label_w=300,
        note="lines of source, excluding vendor and node_modules"))
    return made


def main():
    os.makedirs(FIG, exist_ok=True)
    made = survey_figures() + evaluation_figures() + repository_figures()
    for path in made:
        print("  ", os.path.relpath(path, ROOT))
    print(f"\n{len(made)} charts written to {os.path.relpath(FIG, ROOT)}")


if __name__ == "__main__":
    main()
