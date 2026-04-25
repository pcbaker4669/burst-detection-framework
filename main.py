# main.py

from scripts.load_data import load_all_summaries
from scripts.compute_bursts import add_burst_flag
from scripts.plot_distributions import plot_ccdf, plot_hist, plot_lorenz

def main():
    print("Running burst analysis...\n")

    # 1. Load data
    df = load_all_summaries("derived")
    print("Total rows:", len(df))
    print("Columns:", list(df.columns))

    # 2. Basic stats
    print("\nMax Score Rate Stats:")
    print(df["max_score_rate"].describe())

    # 3. Add burst flag
    df = add_burst_flag(df)

    # 4. Burst summary
    burst_pct = df["is_burst"].mean()
    print("\nBurst %:", burst_pct)

    burst_comments = df[df["is_burst"]]["total_dcomments"].sum()
    total_comments = df["total_dcomments"].sum()

    if total_comments > 0:
        print("Share of comments from bursts:", burst_comments / total_comments)

    # 5. Plot
    plot_hist(
        df["max_score_rate"],
        "figures/fig2_hist_max_score_rate.png")
    plot_ccdf(
        df["max_score_rate"],
        "figures/fig1_ccdf_max_score_rate.png"
    )
    plot_lorenz(df["total_dcomments"], "figures/fig3_lorenz.png")

    # 6. Show top bursts
    print("\nTop 10 burst posts:")
    print(df.sort_values("max_score_rate", ascending=False).head(10))

if __name__ == "__main__":
    main()