import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["font.size"] = 28
matplotlib.rcParams["font.family"] = "sans-serif"

RED = "#d20000"
GREEN = "#007355"
BLUE = "#007aff"
BAR_WIDTH = 0.6
LABELS = ["Cost", "Payoff"]


def make_bar(cost, payoff, filename):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.bar(LABELS, [cost, payoff], color=[RED, GREEN], width=BAR_WIDTH, edgecolor="none")
    ax.set_ylim(0, 12)
    ax.set_xlim(-0.6, 1.6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_yticks([])
    ax.tick_params(axis="x", length=0, pad=10)
    fig.tight_layout()
    fig.savefig(filename, dpi=150, bbox_inches="tight", transparent=True)
    plt.close(fig)


def make_stacked_bar(cost, payoff_green, payoff_blue, filename):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.bar(LABELS[0], cost, color=RED, width=BAR_WIDTH, edgecolor="none")
    ax.bar(LABELS[1], payoff_green, color=GREEN, width=BAR_WIDTH, edgecolor="none")
    ax.bar(LABELS[1], payoff_blue, bottom=payoff_green, color=BLUE, width=BAR_WIDTH, edgecolor="none")
    ax.set_ylim(0, 12)
    ax.set_xlim(-0.6, 1.6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_yticks([])
    ax.tick_params(axis="x", length=0, pad=10)
    fig.tight_layout()
    fig.savefig(filename, dpi=150, bbox_inches="tight", transparent=True)
    plt.close(fig)


make_bar(cost=8, payoff=3, filename="01_high_cost_low_payoff.png")
make_bar(cost=8, payoff=10, filename="02_high_cost_high_payoff.png")
make_bar(cost=3, payoff=10, filename="03_low_cost_high_payoff.png")
make_stacked_bar(cost=8, payoff_green=3, payoff_blue=7, filename="04_grade_boost.png")
make_stacked_bar(cost=2, payoff_green=3, payoff_blue=7, filename="05_low_cost_grade_boost.png")
make_stacked_bar(cost=2, payoff_green=3, payoff_blue=0, filename="06_low_cost_no_grade.png")
