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
    # Order doesn't matter in marimo

    This notebook recreates the scenarios from the Jupyter
    out-of-order execution demo. In marimo, none of those pitfalls
    occur because running a cell automatically re-runs all of the cells that
    depend upon it.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Example 1: Stale values can't happen
    """)
    return


@app.cell
def _():
    x = 42
    return (x,)


@app.cell
def _(x):
    y = x * 2
    y
    return (y,)


@app.cell
def _(y):
    z = y + 10
    z
    return


@app.cell
def _(mo):
    mo.md("""
    Notice the order of the three cells above: `x` is defined before `y` which is defined before `z`. Try running them from top to bottom to get a result. Suppose we were then to change `x` to 5. In a Jupyter notebook, the values of `y` and `z` would *not* be automatically updated; this behavior is the root cause of many Jupyter notebook bugs. Try it in marimo: you'll see that changing `x` also changes `y` and `z`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Example 2: Non-idempotent cells can't happen

    In the Jupyter demo, this kept incrementing every time it ran:

    ```python
    # Cell A
    count = 0

    # Cell B
    count = count + 1
    ```

    Marimo refuses this statically. Cell B redefines `count`, but
    `count` is already declared in Cell A — marimo flags it as a
    *multiple-definitions* error. The same applies to the
    `items.append("hello")` cell from the Jupyter demo: mutating a
    variable defined in another cell is a static error.

    The only way to make `count` depend on `count` is to do it
    inside a single cell. And running a single cell twice in marimo
    always produces the same output, because the cell is a function
    of its declared inputs.
    """)
    return


@app.cell
def _():
    count = 0
    return (count,)


@app.cell
def _():
    count = count + 1
    return (count,)


@app.cell
def _(mo):
    mo.md("""
    ## Example 3: Ghosts of deleted cells can't happen

    In Jupyter, deleting a cell leaves the variables it defined
    sitting in the kernel's memory. The notebook still appears to
    work — until someone restarts the kernel and gets a `NameError`.

    In marimo, deleting a cell immediately removes its outputs from
    the namespace. Every cell that depended on those outputs is
    re-run and surfaces a clear error right away. There is no
    hidden state.
    """)
    return


@app.cell
def _():
    foo = 10
    return (foo,)


@app.cell
def _(foo):
    bar = foo + 10
    bar
    return


@app.cell
def _():
    ## Example 4: Global variables can't be defined/redefined in multiple cells
    return


@app.cell
def _():
    effective_tax_rate = 0.22
    return (effective_tax_rate,)


@app.cell
def _():
    income = 100_000
    return (income,)


@app.cell
def _():
    effective_tax_rate = .25
    return (effective_tax_rate,)


@app.cell
def _(effective_tax_rate, income):
    taxes = income * effective_tax_rate
    taxes
    return


@app.cell
def _():
    fruits = ["apple", "banana", "orange"]
    fruits.append("lemon")
    return (fruits,)


@app.cell
def _(fruits):
    fruits.append("lemon")
    return


if __name__ == "__main__":
    app.run()
