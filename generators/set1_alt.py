import os
import numpy as np
import matplotlib.pyplot as plt


def make_viz(output_folder: str = "out", export_dpi: int = 200) -> None:
    os.makedirs(output_folder, exist_ok=True)

    def save_figure(fig, filename) -> str:
        path = os.path.join(output_folder, filename)
        fig.tight_layout()
        fig.savefig(path, dpi=export_dpi, bbox_inches="tight")
        plt.close(fig)
        return path

    items = []
    items += _build_set1_three(save_figure)

    questions_path = _write_questions(output_folder, items)

    print(f"Saved files to: {os.path.abspath(output_folder)}")
    print(f"Questions file: {os.path.abspath(questions_path)}")
    for image_path, _, _ in items:
        print(" -", os.path.basename(image_path))


def _build_set1_three(save_figure):
    district_names = ["Riverton", "Northvale", "Marigold", "Eastpoint", "Cedar Bay", "Doverfield"]
    broken_hydrant_percent = np.array([12.18, 12.77, 12.43, 12.59, 12.00, 12.52], dtype=float)

    y_min, y_max = 11.90, 13.10
    y_ticks = np.arange(y_min, y_max + 1e-9, 0.05)

    # 1) No aids
    fig, ax = plt.subplots(figsize=(8.6, 4.0))
    ax.bar(district_names, broken_hydrant_percent, width=0.7)
    ax.set_ylim(y_min, y_max)
    ax.set_yticks(y_ticks)
    ax.grid(axis="y", alpha=0.0)
    ax.set_title("Set 1A — Broken Fire Hydrants (No Aids)")
    ax.tick_params(axis="x", rotation=20)
    p1 = save_figure(fig, "set1_no_aids.png")

    # 2) Horizontal gridlines
    fig, ax = plt.subplots(figsize=(8.6, 4.0))
    ax.bar(district_names, broken_hydrant_percent, width=0.7)
    ax.set_ylim(y_min, y_max)
    ax.set_yticks(y_ticks)
    ax.grid(axis="y", alpha=0.35)
    ax.set_title("Set 1B — Broken Fire Hydrants (Gridlines)")
    ax.tick_params(axis="x", rotation=20)
    p2 = save_figure(fig, "set1_gridlines.png")

    # 3) Fill bar aid (100% reference bar behind each bar)
    # Here we use the same y-scale and draw a faint full-height bar for each category,
    # then draw the real bar on top. This makes "how full is the bar" easier to judge.
    fig, ax = plt.subplots(figsize=(8.6, 4.0))
    x = np.arange(len(district_names))
    full_height = np.full_like(x, y_max, dtype=float)
    ax.bar(x, full_height, width=0.7, bottom=0.0, alpha=0.15)  # background "100%" frame
    ax.bar(x, broken_hydrant_percent, width=0.7)
    ax.set_xticks(x, district_names)
    ax.set_ylim(y_min, y_max)
    ax.set_yticks(y_ticks)
    ax.grid(axis="y", alpha=0.0)
    ax.set_title("Set 1C — Broken Fire Hydrants (Fill Bar Aid)")
    ax.tick_params(axis="x", rotation=20)
    p3 = save_figure(fig, "set1_fillbar.png")

    # Question + answer key (you can adjust wording - is ignored in .gitignore, record survey answers on your own)
    question = "Which percent difference is larger: Riverton vs Northvale, or Cedar Bay vs Doverfield?"
    answer = "Riverton vs Northvale"  # 12.77-12.18=0.59 vs 12.52-12.00=0.52

    return [
        (p1, question, answer),
        (p2, question, answer),
        (p3, question, answer),
    ]


def _write_questions(output_folder, items) -> str:
    path = os.path.join(output_folder, "set1_questions.txt")
    lines = ["Questions and answer key\n"]

    for idx, (image_path, question, answer) in enumerate(items, start=1):
        lines.append(f"{idx}. {os.path.basename(image_path)}")
        lines.append(f"   Q: {question}")
        lines.append(f"   Correct: {answer}")
        lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return path
