from scripts.load_data import load_all_summaries
from scripts.compute_bursts import add_burst_flag
from scripts.plot_distributions import plot_ccdf, plot_hist, plot_lorenz
import numpy as np

def main():
    print("Running burst analysis...\n")

    # 1. Load data
    df = load_all_summaries("derived")
    print("Total rows before deduplication:", len(df))

    # Deduplicate posts by keeping the row with the highest observed max_score_rate
    df = df.sort_values("max_score_rate", ascending=False)
    df = df.drop_duplicates(subset=["post_id"], keep="first")
    df = df.reset_index(drop=True)

    print("Total unique posts after deduplication:", len(df))
    print("Columns:", list(df.columns))

    # 2. Basic stats
    print("\n=== BASIC STATS ===")
    print(df["max_score_rate"].describe())

    # 3. Add burst flag
    df = add_burst_flag(df)

    # 4. Burst summary
    print("\n=== BURST SUMMARY ===")
    burst_pct = df["is_burst"].mean()
    print("Burst %:", burst_pct)

    burst_comments = df[df["is_burst"]]["total_dcomments"].sum()
    total_comments = df["total_dcomments"].sum()

    if total_comments > 0:
        print("Share of comments from bursts:", burst_comments / total_comments)

    # =========================
    # APPENDIX OUTPUT SECTION
    # =========================
    print("\n==============================")
    print("APPENDIX A: DATASET OVERVIEW")
    print("==============================")

    print("Total posts:", len(df))
    print("Unique subreddits:", df["subreddit"].nunique())
    print("Sources:", df["source"].unique())

    print("\n--- Observations per post ---")
    print("Mean:", df["n_observations"].mean())
    print("Median:", df["n_observations"].median())
    print("Min:", df["n_observations"].min())
    print("Max:", df["n_observations"].max())

    print("\n--- Lifespan (seconds) ---")
    print("Mean:", df["lifespan_seconds"].mean())
    print("Median:", df["lifespan_seconds"].median())
    print("Min:", df["lifespan_seconds"].min())
    print("Max:", df["lifespan_seconds"].max())

    print("\n==============================")
    print("APPENDIX A: DISTRIBUTION STATS")
    print("==============================")

    print(df["max_score_rate"].describe())

    print("\n==============================")
    print("APPENDIX A: TAIL BEHAVIOR")
    print("==============================")

    print("> 1.0:", np.sum(df["max_score_rate"] > 1.0))
    print("> 2.0:", np.sum(df["max_score_rate"] > 2.0))
    print("> 3.0:", np.sum(df["max_score_rate"] > 3.0))

    print("\n==============================")
    print("APPENDIX A: GROUP COMPARISONS")
    print("==============================")

    print("\n--- By Subreddit (mean max_score_rate) ---")
    print(df.groupby("subreddit")["max_score_rate"].mean())

    print("\n--- By Source (mean max_score_rate) ---")
    print(df.groupby("source")["max_score_rate"].mean())

    # =========================
    # PLOTS
    # =========================
    plot_hist(
        df["max_score_rate"],
        "figures/fig2_hist_max_score_rate.png"
    )

    plot_ccdf(
        df["max_score_rate"],
        "figures/fig1_ccdf_max_score_rate.png"
    )

    plot_lorenz(
        df["total_dcomments"],
        "figures/fig3_lorenz.png"
    )

    # =========================
    # TOP BURSTS (debug only)
    # =========================
    print("\nTop 10 burst posts:")
    print(df.sort_values("max_score_rate", ascending=False).head(10))


if __name__ == "__main__":
    main()