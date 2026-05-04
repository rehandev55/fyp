import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("data/token_usage.jsonl")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

# gpt-4o-mini pricing (per 1M tokens)
PRICING = {
    "gpt-4o-mini": {
        "input":  0.150,
        "output": 0.600,
    },
    "gpt-4o": {
        "input":  2.50,
        "output": 10.00,
    },
    "text-embedding-3-small": {
        "input":  0.020,
        "output": 0.000,
    }
}

def log_token_usage(
    endpoint:          str,
    model:             str,
    board:             str,
    class_level:       str,
    subject:           str,
    prompt_tokens:     int,
    completion_tokens: int,
):
    """Log token usage and cost for every API call."""
    pricing     = PRICING.get(model, {"input": 0, "output": 0})
    input_cost  = (prompt_tokens     / 1_000_000) * pricing["input"]
    output_cost = (completion_tokens / 1_000_000) * pricing["output"]
    total_cost  = round(input_cost + output_cost, 8)

    record = {
        "timestamp":          datetime.now().isoformat(),
        "endpoint":           endpoint,
        "model":              model,
        "board":              board,
        "class_level":        class_level,
        "subject":            subject,
        "prompt_tokens":      prompt_tokens,
        "completion_tokens":  completion_tokens,
        "total_tokens":       prompt_tokens + completion_tokens,
        "cost_usd":           total_cost
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

    print(f"[TOKENS] {endpoint} | "
          f"prompt={prompt_tokens} "
          f"completion={completion_tokens} "
          f"total={prompt_tokens + completion_tokens} | "
          f"cost=${total_cost:.6f}")