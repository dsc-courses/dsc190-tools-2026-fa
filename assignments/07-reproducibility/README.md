# Assignment 07: Reproducible Data Pipelines

**Due**: Tuesday, November 17 at 11:59 PM on Gradescope

This week's lectures introduced two tools designed to keep data analyses
*reproducible*. **DVC (Data Version Control)** extends git with *data
pipelines* -- named stages with declared inputs and outputs that DVC reruns
automatically whenever an input changes. **Marimo** is a notebook format
that, unlike Jupyter, stores notebooks as plain Python files and executes
cells in dependency order, sidestepping the hidden-state and
version-control issues inherent with `.ipynb` files.

In this assignment, you'll use both together to build a small reproducible
analysis: a multi-stage DVC pipeline that processes a raw dataset, and a
Marimo notebook that loads the pipeline's output and plots it.

## The Dataset

The raw data is provided at `data/raw/events.csv`. Each row is a single
timestamped event, with the columns:

```
user_id,timestamp,event_type,duration_seconds
```

The data is messy: some rows are missing fields, some have non-positive
`duration_seconds`, some have invalid `event_type` values, and timestamps
appear in a few different formats. The first thing your pipeline will do is
clean it up.

## Requirements

Your project should:

1. Be a public GitHub repo, managed with **`uv`**, with its `pyproject.toml`
   and `uv.lock` committed. The autograder runs DVC with `uv run dvc`, so
   `dvc` must be one of your project's dependencies (`uv add dvc`), along
   with anything your scripts and notebook import.

2. Initialize **DVC** with `dvc init`. You do *not* need to configure a DVC
   remote -- everything will work against the local DVC cache.

3. Commit the raw data file at `data/raw/events.csv` directly to git. In a
   real project you would track the raw data with `dvc add` and push it to
   a DVC remote, but to keep things simple we're skipping the remote step
   entirely. DVC will still manage every *derived* file (everything produced
   by your pipeline) automatically.

4. Define a pipeline in **`dvc.yaml`** with at least three stages:

   - **clean** -- reads `data/raw/events.csv`, drops rows that have any missing
     fields, an invalid `event_type`, or a non-positive `duration_seconds`, and
     normalizes `timestamp` to ISO 8601 (that is, to the format
     `YYYY-MM-DDTHH:MM:SS`). Keep `duration_seconds` as a whole number
     (e.g., `45`, not `45.0`). This stage should write its result to
     `data/clean/events.csv`.

   - **transform** -- reads `data/clean/events.csv` and adds a `date`
     column containing the date portion of `timestamp` in `YYYY-MM-DD`
     format. Writes the result to `data/transformed/events.csv`.

   - **features** -- reads `data/transformed/events.csv` and adds two
     new columns to each row:

     - `duration_minutes`: the event's `duration_seconds` divided by
       60.
     - `weekday`: the day-of-week name of the event's `date`, written
       in full (e.g., `Monday`, `Tuesday`, ..., `Sunday`).

     Writes the result to `data/features/events.csv`, with the original
     columns plus the two new ones. The number of rows should be
     unchanged from `data/transformed/events.csv`.

5. Running `dvc repro` from a fresh clone of your repository should
   regenerate every output under `data/clean/`, `data/transformed/`, and
   `data/features/`.

6. Include a **Marimo notebook** at `notebooks/report.py` that loads
   `data/features/events.csv` and produces a histogram of the
   **`duration_minutes`** column, showing the distribution of event
   durations across the dataset.

## The Autograder

Submit to the autograder a single file named `repo_url.txt` containing the
URL of your public GitHub repository.

The autograder will:

- Clone your repo and run `uv sync`.
- Run `dvc repro` and check that every stage succeeds.
- Check that `data/features/events.csv` exists, has the expected
  columns (the original four plus `date`, `duration_minutes`, and
  `weekday`), and contains the correct feature values for a known set
  of input rows.
- Check that `notebooks/report.py` is a Marimo notebook (a Python file
  that imports `marimo` and parses cleanly).

All of the autograder's checks are public, so if you pass all of them, you
will get full credit on this assignment.
