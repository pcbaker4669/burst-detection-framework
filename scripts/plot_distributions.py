# scripts/plot_distributions.py

import matplotlib.pyplot as plt
import numpy as np

import numpy as np
import matplotlib.pyplot as plt

def plot_ccdf(series, path):
    values = series.dropna()
    values = values[values >= 0]
    x = np.sort(values.to_numpy())

    n = len(x)
    y = 1.0 - (np.arange(1, n + 1) / n)
    y = np.maximum(y, 1 / n)

    plt.figure(figsize=(7, 5))
    plt.plot(x, y, linewidth=2)

    plt.yscale("log")

    plt.xlabel("Maximum score growth rate")
    plt.ylabel("Share of posts with rate ≥ x")
    plt.title("Tail Distribution of Post Growth Rates")

    plt.grid(True, which="both", linewidth=0.4, alpha=0.4)

    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()

def plot_hist(series, path):
    data = series.dropna()
    data = data[data < 1.0]  # clip extreme tail

    plt.figure(figsize=(7, 5))
    plt.hist(data, bins=50)

    plt.xlabel("Maximum score growth rate")
    plt.ylabel("Number of posts")
    plt.title("Distribution of Post Growth Rates")

    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()

def plot_lorenz(series, path):
    x = np.sort(series.dropna())
    cumulative = np.cumsum(x)
    cumulative = cumulative / cumulative[-1]

    n = len(x)
    population = np.arange(1, n + 1) / n

    plt.figure(figsize=(6,6))
    plt.plot(population, cumulative, label="Observed")
    plt.plot([0,1], [0,1], linestyle="--", label="Equal distribution")

    plt.xlabel("Cumulative share of posts")
    plt.ylabel("Cumulative share of comments")
    plt.title("Concentration of Comment Activity")

    plt.legend()
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()