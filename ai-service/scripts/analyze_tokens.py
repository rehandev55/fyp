import json
from pathlib import Path
from datetime import datetime

LOG_FILE = Path("data/token_usage.jsonl")

def analyze():
    if not LOG_FILE.exists():
        print("No token usage log found.")
        return

    records = []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    if not records:
        print("Log file is empty.")
        return

    total_cost       = sum(r["cost_usd"] for r in records)
    total_tokens     = sum(r["total_tokens"] for r in records)
    total_prompt     = sum(r["prompt_tokens"] for r in records)
    total_completion = sum(r["completion_tokens"] for r in records)
    total_calls      = len(records)

    print("=" * 50)
    print("TOKEN USAGE REPORT")
    print("=" * 50)
    print(f"Total API calls:       {total_calls}")
    print(f"Total tokens:          {total_tokens:,}")
    print(f"  Prompt tokens:       {total_prompt:,}")
    print(f"  Completion tokens:   {total_completion:,}")
    print(f"Total cost:            ${total_cost:.4f}")
    print()

    # breakdown by endpoint
    print("── By endpoint ──────────────────────────────")
    by_endpoint = {}
    for r in records:
        e = r["endpoint"]
        if e not in by_endpoint:
            by_endpoint[e] = {"calls": 0, "tokens": 0, "cost": 0}
        by_endpoint[e]["calls"]  += 1
        by_endpoint[e]["tokens"] += r["total_tokens"]
        by_endpoint[e]["cost"]   += r["cost_usd"]

    for endpoint, data in sorted(by_endpoint.items()):
        print(f"  {endpoint:20} "
              f"calls={data['calls']:4} "
              f"tokens={data['tokens']:8,} "
              f"cost=${data['cost']:.4f}")

    print()

    # breakdown by subject
    print("── By subject ───────────────────────────────")
    by_subject = {}
    for r in records:
        s = r["subject"]
        if s not in by_subject:
            by_subject[s] = {"calls": 0, "cost": 0}
        by_subject[s]["calls"] += 1
        by_subject[s]["cost"]  += r["cost_usd"]

    for subject, data in sorted(by_subject.items(),
                                key=lambda x: -x[1]["cost"]):
        print(f"  {subject:15} "
              f"calls={data['calls']:4} "
              f"cost=${data['cost']:.4f}")

    print()

    # most expensive single call
    most_expensive = max(records, key=lambda r: r["cost_usd"])
    print("── Most expensive single call ───────────────")
    print(f"  Endpoint:  {most_expensive['endpoint']}")
    print(f"  Subject:   {most_expensive['subject']}")
    print(f"  Tokens:    {most_expensive['total_tokens']:,}")
    print(f"  Cost:      ${most_expensive['cost_usd']:.6f}")
    print(f"  Time:      {most_expensive['timestamp']}")
    print("=" * 50)


if __name__ == "__main__":
    analyze()