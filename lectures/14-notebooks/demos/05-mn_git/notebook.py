import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # marimo notebooks are Python files

    Open this notebook file (`notebook.py`) in any plain text editor, and you'll see ordinary Python (with some `marimo` syntactic sugar). This is in contrast with Jupyter notebooks (which as JSON). As a consequence, Marimo notebooks are easier to version control.
    """)
    return


@app.cell
def _():
    import datetime
    import math

    import matplotlib.pyplot as plt

    return datetime, math, plt


@app.cell
def _(datetime, math, plt):
    now = datetime.datetime.now()
    secs = now.hour * 3600 + now.minute * 60 + now.second
    phase = (secs % 60) / 60.0 * 2 * math.pi

    xs = list(range(50))
    ys = [math.sin(0.3 * x + phase) for x in xs]

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(xs, ys, marker="o", markersize=3)
    ax.set_title(f"sin(0.3*x + phase) at {now.strftime('%H:%M:%S')}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    fig.tight_layout()
    fig
    return


@app.cell
def _(mo):
    mo.md("""
    The plot above depends on the current time, so the picture changes every time the cell runs. But the notebook file is unchanged — the plot output lives only in the marimo UI, not in `notebook.py`.

    Try it:

    1. Make sure this file is committed to git as-is (it already is if you cloned the course repo).
    2. Open the notebook in marimo and let it run.
    3. Run `git diff notebook.py` in a terminal.

    The diff is empty. The plot rendered, but nothing about the file changed. Contrast this with the Jupyter `noisy_diffs.ipynb` demo, where the same operation produced a massive diff full of base64.
    """)
    return


if __name__ == "__main__":
    app.run()
