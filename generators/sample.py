import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def make_viz((output_folder: str = "weber_stimuli_out", export_dpi: int = 200) -> None:
    """
    Generates 6 Weber’s Law stimulus images (3 pairs) and a questions.txt file.

    Output:
      <output_folder>/
        V1_bar_no_aids.png
        V2_bar_gridlines.png
        V3_line_no_aids.png
        V4_line_gridlines.png
        V5_dots_no_aids.png
        V6_dots_boxes.png
        questions.txt
    """
    os.makedirs(output_folder, exist_ok=True)

    def save_figure(fig, filename) -> str:
        path = os.path.join(output_folder, filename)
        fig.tight_layout()
        fig.savefig(path, dpi=export_dpi, bbox_inches="tight")
        plt.close(fig)
        return path

    items = []
    items += _build_bar_pair(save_figure)
    items += _build_line_pair(save_figure)
    items += _build_dot_count_pair(save_figure)

    questions_path = _write_questions(output_folder, items)

    print(f"Saved files to: {os.path.abspath(output_folder)}")
    print(f"Questions file: {os.path.abspath(questions_path)}")
    for image_path, _, _ in items:
        print(" -", os.path.basename(image_path))


def _build_bar_pair(save_figure):
    value_a = 64
    value_b = 66  # correct: B

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(["A", "B"], [value_a, value_b])
    ax.set_ylim(55, 75)
    ax.set_title("V1 — Bar (No Aids)")
    p1 = save_figure(fig, "V1_bar_no_aids.png")

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(["A", "B"], [value_a, value_b])
    ax.set_ylim(55, 75)
    ax.set_yticks(np.arange(55, 76, 1))
    ax.grid(axis="y", alpha=0.6)
    ax.set_title("V2 — Bar (Gridlines)")
    p2 = save_figure(fig, "V2_bar_gridlines.png")

    return [
        (p1, "Which bar is larger? (A or B)", "B"),
        (p2, "Which bar is larger? (A or B)", "B"),
    ]


def _build_line_pair(save_figure):
    x_values = np.arange(1, 11)

    line_a = np.array([32, 33, 33, 32, 33, 34, 34, 33, 32, 33], dtype=float)
    line_b = np.array([32, 32, 33, 32, 33, 34, 35, 33, 32, 33], dtype=float)  # B higher at x=7

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(x_values, line_a, marker="o", label="A")
    ax.plot(x_values, line_b, marker="o", label="B")
    ax.set_xticks(x_values)
    ax.set_ylim(30, 37)
    ax.set_title("V3 — Line (No Aids)")
    ax.legend(frameon=False)
    p3 = save_figure(fig, "V3_line_no_aids.png")

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(x_values, line_a, marker="o", label="A")
    ax.plot(x_values, line_b, marker="o", label="B")
    ax.set_xticks(x_values)
    ax.set_yticks(np.arange(30, 38, 1))
    ax.set_ylim(30, 37)
    ax.grid(True, alpha=0.5)
    ax.set_title("V4 — Line (Gridlines)")
    ax.legend(frameon=False)
    p4 = save_figure(fig, "V4_line_gridlines.png")

    return [
        (p3, "At x = 7, which line is higher? (A or B)", "B"),
        (p4, "At x = 7, which line is higher? (A or B)", "B"),
    ]


def _build_dot_count_pair(save_figure):
    count_a = 57
    count_b = 60  # correct: B

    def points_for_group(n, x_offset):
        columns = 10
        xs, ys = [], []
        for idx in range(n):
            row, col = divmod(idx, columns)
            xs.append(x_offset + col)
            ys.append(row)
        return np.array(xs), np.array(ys)

    ax_x, ax_y = points_for_group(count_a, x_offset=0)
    bx_x, bx_y = points_for_group(count_b, x_offset=14)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.scatter(ax_x, ax_y, s=20)
    ax.scatter(bx_x, bx_y, s=20)
    ax.set_title("V5 — Dot Counts (No Aids)")
    ax.set_xticks([4.5, 18.5], ["A", "B"])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xlim(-2, 26)
    ax.set_ylim(-1, max(ax_y.max(), bx_y.max()) + 2)
    p5 = save_figure(fig, "V5_dots_no_aids.png")

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.scatter(ax_x, ax_y, s=20)
    ax.scatter(bx_x, bx_y, s=20)
    ax.set_title("V6 — Dot Counts (Boxes)")
    ax.set_xticks([4.5, 18.5], ["A", "B"])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xlim(-2, 26)
    ax.set_ylim(-1, max(ax_y.max(), bx_y.max()) + 2)

    ax.add_patch(Rectangle((-0.8, -0.8), 11.6, 7.2, fill=False, linewidth=2, alpha=0.7))
    ax.add_patch(Rectangle((13.2, -0.8), 11.6, 7.2, fill=False, linewidth=2, alpha=0.7))
    p6 = save_figure(fig, "V6_dots_boxes.png")

    return [
        (p5, "Which group has more dots? (A or B)", "B"),
        (p6, "Which group has more dots? (A or B)", "B"),
    ]


def _write_questions(output_folder, items) -> str:
    path = os.path.join(output_folder, "questions.txt")
    lines = ["Questions and answer key\n"]

    for idx, (image_path, question, answer) in enumerate(items, start=1):
        lines.append(f"{idx}. {os.path.basename(image_path)}")
        lines.append(f"   Q: {question}")
        lines.append(f"   Correct: {answer}")
        lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return path
