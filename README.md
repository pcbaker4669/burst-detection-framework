[![DOI](https://zenodo.org/badge/1220916325.svg)](https://doi.org/10.5281/zenodo.20010106)

# Burst Detection Framework

A measurement framework for detecting high-velocity events in time-resolved social media data. This project reconstructs post growth trajectories from repeated observations and identifies burst-like behavior using simple, interpretable rate-based metrics.

---

## Overview

Most analyses of online engagement rely on static measures such as total score or comment count. This framework instead tracks posts over time and computes growth rates to capture how attention evolves.

The goal is to identify high-velocity events—posts that experience rapid, short-term increases in engagement—and to measure their contribution to overall activity.

This repository contains the analysis code used to generate the figures and results for a study of burst dynamics in Reddit data.

---

## Key Concepts

- Time-resolved tracking: Posts are observed repeatedly over time
- Growth rates: Engagement is measured as change per unit time
- Burst detection: High-velocity events are identified using a simple threshold rule
- Concentration: A small fraction of posts may account for a large share of activity

---

## Method Summary

For each post:

1. Observations are grouped and ordered by time
2. Growth rates are computed between consecutive observations
3. Summary metrics are derived, including:
   - average growth rate
   - maximum growth rate

A post is classified as a burst event if:

max_score_rate > 0.4

This threshold isolates posts exhibiting extreme short-term growth relative to the overall distribution.

---

## Repository Structure

burst-detection-framework/
├── scripts/
│   ├── load_data.py
│   ├── compute_bursts.py
│   ├── plot_distributions.py
├── main.py
├── figures/
├── data_sample/
├── derived_sample/
├── README.md
├── .gitignore

---

## Usage

Run the analysis:

python main.py

This will:

- load summary data
- compute burst classifications
- generate figures:
  - CCDF (tail distribution)
  - histogram (distribution shape)
  - Lorenz curve (concentration)

---

## Reproducibility

A small sample dataset is included in derived_sample/ to allow reproduction of the figures. The full dataset is not included due to size constraints.

---

## Results (Summary)

Analysis of the dataset shows:

- Strong right-skew in growth rates
- Heavy-tailed behavior in the upper distribution
- Approximately 9% of posts account for roughly 60% of total comment activity

These findings indicate that online attention is driven by a small number of high-velocity events.

---

## Related Project

Reddit JSON Collector  
A companion repository for collecting time-resolved Reddit data using public JSON endpoints.

---

## Citation

(Update after adding your Zenodo DOI)

Baker, P. (2026). Burst Detection Framework (Version X.X.X) [Computer software].

---

## License

MIT License (or specify your preferred license)