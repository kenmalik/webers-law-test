import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def make_viz():
    data = load_data()

    _, ax = plt.subplots(figsize=(8, 8))

    ax.bar(data.index, data)
    ax.set_title("Top 15 US Universities International Student Ratios")
    ax.set_xticks(data.index)
    ax.set_xticklabels(data.index, rotation=45, ha="right")
    ax.set_ylabel("International Student Percentage")

    plt.tight_layout()
    plt.savefig("set2-no-aid.png")

    ax.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig("set2-horizontal-lines.png")

    ax.grid(False)
    ax.bar(data.index, np.full((len(data)), 100) - data, bottom=data, color="lightblue")
    plt.savefig("set2-fill-bar.png")


def load_data():
    data = pd.read_csv("data/US_Top_50_Universities_2026.csv")
    data.set_index("University_Name", inplace=True)
    return data.nlargest(15, "National_Rank")["Intl_Student_Ratio"]
