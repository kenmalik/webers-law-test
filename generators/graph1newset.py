import matplotlib.pyplot as plt
import numpy as np
import os

def make_viz(output_folder: str = 'out', export_dpi: int = 200) -> None:
    os.makedirs(output_folder, exist_ok=True)

    def save_figure(fig, filename) -> str:
        path = os.path.join(output_folder, filename)
        fig.tight_layout()
        fig.savefig(path, dpi=export_dpi, bbox_inches='tight')
        plt.close(fig)
        return path
    
    items = _build_graph_set(save_figure)
    _write_questions(output_folder, items)

def _build_graph_set(save_figure):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    x_values = np.arange(len(days))
    week1 = np.array([2100, 1950, 2400, 2200, 2800, 2950, 2600], dtype=float)

    y_min, y_max = 1500, 3500
    y_ticks = np.arange(y_min, y_max + 1, 200)

    # Basic Bar Graph (No Aids)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(days, week1, color='#4B3621', label="Week A")
    ax.set_ylim(y_min, y_max)
    ax.set_yticks(y_ticks)
    ax.set_title("Coffee Shop Gross Sales (No Aids)", fontsize=12)
    ax.set_ylabel("Gross Sales ($)")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    p1 = save_figure(fig, 'coffeeRevenue_bars_no_aids.png')
    q1 = "Which day of the week had the lowest gross sales?"
    ans1 = "Tuesday"

    # Bar Graph with Gridlines
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(days, week1, color='#4B3621', label="Week A")
    ax.set_ylim(y_min, y_max)
    ax.set_yticks(y_ticks)
    ax.grid(axis='y', alpha=0.3, color='gray', linestyle='-') 
    ax.set_title("Coffee Shop Gross Sales (Gridlines)", fontsize=12)
    ax.set_ylabel("Gross Sales ($)")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    p2 = save_figure(fig, 'coffeeRevenue_bars_grid.png')
    q2 = "According to the grid, approximately how much more revenue was made on Friday compared to Thursday?"
    ans2 = "$600"

    # Bar Graph with Fill Bar Aid
    fig, ax = plt.subplots(figsize=(7, 4))
    
    # Background "100%" frame bars (represents the max potential height)
    full_height = np.full_like(x_values, y_max, dtype=float)
    ax.bar(x_values, full_height, color='#4B3621', alpha=0.15) 
    
    # Primary data bars drawn over the frame
    ax.bar(x_values, week1, color='#4B3621', label='Week A')

    ax.set_xticks(x_values)
    ax.set_xticklabels(days)
    ax.set_ylim(y_min, y_max)
    ax.set_yticks(y_ticks)
    ax.set_title("Coffee Shop Gross Sales (Fill Bar Aid)", fontsize=12)
    ax.set_ylabel("Gross Sales ($)")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    p3 = save_figure(fig, 'coffeeRevenue_bars_fill_aid.png')
    q3 = "Which revenue difference is larger: Monday vs Tuesday, or Saturday vs Sunday?"
    ans3 = "Saturday vs Sunday"

    return [(p1, q1, ans1), (p2, q2, ans2), (p3, q3, ans3)]

def _write_questions(output_folder, items) -> str:
    path = os.path.join(output_folder, 'questions_key.txt')
    with open(path, 'w') as f:
        for idx, (img, q, a) in enumerate(items, 1):
            f.write(f'{idx}. {os.path.basename(img)}\n Q: {q}\n Correct: {a}\n\n')
    return path