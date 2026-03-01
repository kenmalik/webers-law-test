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
    x_values = np.arange(1, 8) 
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    width = 0.35  

    week1 = np.array([2100, 1950, 2400, 2200, 2800, 2950, 2600], dtype=float)
    week2 = np.array([2150, 2020, 2380, 2250, 2850, 3010, 2580], dtype=float)

    question = 'On which day was the revenue gap between Week A and Week B the largest?'
    answer = 'Tuesday'

    # --- 1. Basic Bar Graph (No grid, simple colors) ---
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(x_values - width/2, week1, width, color='#4B3621', label="Week A")
    ax.bar(x_values + width/2, week2, width, color='#6F4E37', label="Week B")

    ax.set_xticks(x_values)
    ax.set_xticklabels(days)
    ax.set_ylim(0, 3500) 
    ax.set_title("Revenue of sales for Coffee Shop", fontsize=12)
    ax.set_ylabel("Gross Sales ($)")
    ax.legend(frameon=False, loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    p1 = save_figure(fig, 'coffeeRevenue_bars_basic.png')

    # --- 2. Bar Graph with Gridlines ---
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(x_values - width/2, week1, width, color='#4B3621', label="Week A")
    ax.bar(x_values + width/2, week2, width, color='#6F4E37', label="Week B")
    
    ax.set_xticks(x_values)
    ax.set_xticklabels(days)
    ax.set_yticks(np.arange(0, 3601, 500))
    ax.grid(axis='y', alpha=0.3, color='gray', linestyle='-') 

    ax.set_title("Revenue of sales for Coffee Shop (Grid Aid)", fontsize=12)
    ax.set_ylabel("Gross Sales ($)")
    ax.legend(frameon=False, loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    p2 = save_figure(fig, 'coffeeRevenue_bars_grid.png')

    # --- 3. Bar Graph with High Contrast & Labels (The "Max Aid" version) ---
    fig, ax = plt.subplots(figsize=(7, 4))
    bar1 = ax.bar(x_values - width/2, week1, width, color='#4B3621', label='Week A')
    bar2 = ax.bar(x_values + width/2, week2, width, color='#E67E22', label='Week B')

    ax.bar_label(bar1, padding=3, fontsize=8)
    ax.bar_label(bar2, padding=3, fontsize=8)

    ax.set_xticks(x_values)
    ax.set_xticklabels(days)
    ax.set_ylim(0, 4000) 
    ax.set_title("Revenue of sales for Coffee Shop (Full Aid)", fontsize=12)
    ax.set_ylabel("Gross Sales ($)")
    ax.legend(frameon=False, loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_yaxis().set_visible(False) 
    p3 = save_figure(fig, 'coffeeRevenue_bars_labels.png')

    return [(p1, question, answer), (p2, question, answer), (p3, question, answer)]

def _write_questions(output_folder, items) -> str:
    path = os.path.join(output_folder, 'questions_key.txt')
    with open(path, 'w') as f:
        for idx, (img, q, a) in enumerate(items, 1):
            f.write(f'{idx}. {os.path.basename(img)}\n Q: {q}\n Correct: {a}\n\n')
    return path
