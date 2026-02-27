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

    week1 = np.array([2100, 1950, 2400, 2200, 2800, 2950, 2600], dtype=float)
    week2 = np.array([2150, 2020, 2380, 2250, 2850, 3010, 2580], dtype=float)

    # question/answer info to be saved which visualizations
    question = 'On which day was the revenue gap between Week A and Week B the largest?'
    answer = 'Tuesday'

    # first line graph with no aids, just two lines representing different weeks
    fig, ax = plt.subplots(figsize=(7, 4))

    # marker (dots) aren't added on each x-axis label
    ax.plot(x_values, week1, color='#4B3621', label="Week A")
    ax.plot(x_values, week2, color='#6F4E37', label="Week B")

    ax.set_xticks(x_values)
    ax.set_xticklabels(days)
    ax.set_ylim(1500, 3500) 
    ax.set_title("Revenue of sales for Coffee Shop in two unique weeks", fontsize=12)
    ax.set_ylabel("Gross Sales ($)")
    ax.legend(frameon=False, loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    p1 = save_figure(fig, 'coffeeRevenue_no_aids.png')

    # second line graph with gridlines to help visualize/estimate exact sales
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(x_values, week1, marker="o", markersize=5, color='#4B3621', label="Week A")
    ax.plot(x_values, week2, marker="o", markersize=5, color='#6F4E37', label="Week B")
    ax.set_xticks(x_values)
    ax.set_xticklabels(days)
    ax.set_yticks(np.arange(1500, 3600, 200)) 
    ax.set_ylim(1500, 3500)

    # grid added to help estimate values
    ax.grid(True, alpha=0.3, color='gray', linestyle='-')

    ax.set_title("Revenue of sales for Coffee Shop in two unique weeks", fontsize=12)
    ax.set_ylabel("Gross Sales ($)")
    ax.legend(frameon=False, loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    p2 = save_figure(fig, 'coffeeRevenue_gridlines.png')

    # third graph with more unique colors and fill line to discern which line graph
    # made more for each point in the graph
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(x_values, week1, marker='o', markersize=5, color='#4B3621', label='Week A')
    ax.plot(x_values, week2, marker='o', markersize=5, color='#E67E22', label='Week B')

    # fill lines help visualize which week has generally higher revenue
    ax.fill_between(x_values, 1500, week1, color='#4B3621', alpha=.4)
    ax.fill_between(x_values, 1500, week2, color='#E67E22', alpha=.2)

    ax.set_xticks(x_values)
    ax.set_xticklabels(days)
    ax.set_yticks(np.arange(1500, 3600, 100)) 
    ax.set_ylim(1500, 3500)
    ax.grid(True, alpha=0.3, color='gray', linestyle='-')
    ax.set_title("Revenue of sales for Coffee Shop in two unique weeks", fontsize=12)
    ax.set_ylabel("Gross Sales ($)")
    ax.legend(frameon=False, loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    p3 = save_figure(fig, 'coffeeRevenue_fill.png')

    return [(p1, question, answer), (p2, question, answer), (p3, question, answer)]

def _write_questions(output_folder, items) -> str:
    path = os.path.join(output_folder, 'questions_key.txt')
    with open(path, 'w') as f:
        for idx, (img, q, a) in enumerate(items, 1):
            f.write(f'{idx}. {os.path.basename(img)}\n Q: {q}\n Correct: {a}\n\n')
    return path

if __name__ == '__main__':
    make_viz()