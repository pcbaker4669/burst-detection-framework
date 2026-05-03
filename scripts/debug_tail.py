from pathlib import Path
from load_data import load_all_summaries

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DERIVED_DIR = PROJECT_ROOT / "derived"

df = load_all_summaries(DERIVED_DIR)

tail = df[df["max_score_rate"] > 2.0] \
    .sort_values("max_score_rate", ascending=False)

print("\n=== EXTREME TAIL POSTS (> 2.0) ===")
print(tail[["post_id", "max_score_rate", "total_dscore", "total_dt_seconds"]])
print("\nCount:", len(tail))