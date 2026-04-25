# scripts/load_data.py

import pandas as pd
from pathlib import Path

def load_all_summaries(base_dir):
    base = Path(base_dir)

    all_files = list(base.glob("*/*/*/all_post_summary.csv"))

    dfs = []
    for f in all_files:
        df = pd.read_csv(f)
        df["source_file"] = str(f)  # track origin (optional)
        dfs.append(df)

    combined = pd.concat(dfs, ignore_index=True)
    return combined