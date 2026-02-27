import pandas as pd
import matplotlib.pyplot as plt


def make_viz():
    data = load_data()

    _, ax = plt.subplots(figsize=(8, 8))

    ax.bar(data.index, data)
    ax.set_title("Top 10 US Universities International Student Ratios")
    ax.set_xticklabels(data.index, rotation=45, ha="right")
    ax.set_ylabel("International Student Percentage")

    plt.tight_layout()
    plt.show()


def load_data():
    data = pd.read_csv("data/US_Top_50_Universities_2026.csv")
    data.set_index("University_Name", inplace=True)
    return data.nlargest(10, "National_Rank")["Intl_Student_Ratio"]
