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
    # Interactivity and dependencies

    This notebook demonstrates two more marimo features: **interactive UI elements** that plug into the dependency graph, and **automatic dependency management** through inline metadata.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Missing dependencies

    This notebook imports `matplotlib` and `numpy`, but it does not ship with a `requirements.txt` or an inline metadata block declaring them. Open it in a fresh environment where those packages aren't installed and run:

    ```bash
    marimo edit notebook.py
    ```

    When marimo encounters the import statements, it will pop up a prompt in the UI offering to install the missing packages for you. You don't need to drop back to the terminal, figure out the package names, or activate a venv first — marimo handles it from inside the notebook.
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np

    return np, plt


@app.cell
def _(mo):
    mo.md("""
    ## An interactive plot

    The two sliders below control the frequency and phase of a sine wave. Move them and watch the plot update in real time.
    """)
    return


@app.cell
def _(mo):
    frequency = mo.ui.slider(
        start=0.1, stop=2.0, step=0.05, value=0.3, label="frequency"
    )
    phase = mo.ui.slider(
        start=0.0, stop=6.28, step=0.05, value=0.0, label="phase"
    )
    mo.vstack([frequency, phase])
    return frequency, phase


@app.cell
def _(frequency, np, phase, plt):
    xs = np.linspace(0, 20, 200)
    ys = np.sin(frequency.value * xs + phase.value)

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(xs, ys)
    ax.set_title(f"sin({frequency.value:.2f} * x + {phase.value:.2f})")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    fig.tight_layout()
    fig
    return


if __name__ == "__main__":
    app.run()
