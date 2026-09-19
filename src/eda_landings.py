"""eda_landings.py — bootstrap EDA on national landings totals.

Hand-seeded headline numbers from CMFRI 'Marine Fish Landings in India - 2024'
and prior annual reports. Replace with parsed PDF tables in Phase 1.

Outputs figures into ./figures/
"""
from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True, parents=True)

# National marine fish landings, mainland India, million tonnes (CMFRI annual reports).
# To be *verified against parsed PDFs* — treat as bootstrap until Phase 1 parsing lands.
NATIONAL = pd.Series(
    {2019: 3.56, 2020: 2.96, 2021: 3.13, 2022: 3.51, 2023: 3.53, 2024: 3.45},
    name="landings_mt",
)

# Andaman & Nicobar 2024 (CMFRI 2024): 16,674 tonnes
ANDAMAN_2024 = 0.016674  # in Mt


def plot_national_trend() -> None:
    ax = NATIONAL.plot(marker="o", figsize=(7, 4), title="India marine fish landings (mainland)")
    ax.set_ylabel("million tonnes")
    ax.set_xlabel("year")
    ax.grid(alpha=0.3)
    ax.annotate("COVID dip", xy=(2020, 2.96), xytext=(2021, 3.0),
                arrowprops=dict(arrowstyle="->", color="gray"), fontsize=8, color="gray")
    plt.tight_layout()
    out = FIG / "national_landings_trend.png"
    plt.savefig(out, dpi=300)
    print("saved", out.relative_to(ROOT))


if __name__ == "__main__":
    plot_national_trend()
