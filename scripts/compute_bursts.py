# scripts/compute_bursts.py

def add_burst_flag(df, threshold=0.4):
    df["is_burst"] = df["max_score_rate"] > threshold
    return df