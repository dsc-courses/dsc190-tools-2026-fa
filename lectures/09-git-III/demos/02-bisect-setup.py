#!/usr/bin/env python3
"""Create a Git repository for the git bisect demo.

Usage:
    python 02-bisect-setup.py <path>

Initializes a fresh repo at <path> and replays a linear, fourteen-commit history
of a small summary-statistics tool. Commit 8 ("Simplify median") drops the call
to `sorted` in `median`, so every commit from there on reports the wrong median:

    $ python summarize.py data/scores.txt
    ...
    median: 67.00     # should be 83.00

Find the culprit by hand with `git bisect good` / `git bisect bad`, or let git
do it:

    git bisect start HEAD <hash of "Add mean and median">
    git bisect run python -c "from stats import median; assert median([3, 1, 2]) == 2"
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

AUTHOR_NAME = "Sam Okafor"
AUTHOR_EMAIL = "sam@example.com"

README_V1 = """# summarize

Summary statistics for a file of numbers.
"""

README_V2 = README_V1 + """
## Usage

Put one number per line in a text file, then run:

    python summarize.py data/scores.txt
"""

GITIGNORE = "__pycache__/\n"

SCORES = "".join(f"{x}\n" for x in
                 [88, 72, 95, 61, 84, 79, 90, 67, 83, 76, 92, 58, 81, 84, 87])

QUIZ = "".join(f"{x}\n" for x in [7, 9, 4, 10, 8, 6, 9, 5, 8])


# stats.py ---------------------------------------------------------------------

MEAN = '''
def mean(xs):
    return sum(xs) / len(xs)
'''

MEDIAN = '''
def median(xs):
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2
'''

# The bug: the list is never sorted.
MEDIAN_BUGGY = '''
def median(xs):
    n = len(xs)
    mid = n // 2
    if n % 2 == 1:
        return xs[mid]
    return (xs[mid - 1] + xs[mid]) / 2
'''

STD_V1 = '''
def std(xs):
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / len(xs))
'''

VARIANCE = '''
def variance(xs):
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)
'''

STD_V2 = '''
def std(xs):
    return math.sqrt(variance(xs))
'''

MODE = '''
def mode(xs):
    return Counter(xs).most_common(1)[0][0]
'''

RANGE = '''
def value_range(xs):
    return max(xs) - min(xs)
'''


def stats_py(imports, funcs):
    header = '"""Summary statistics for lists of numbers."""\n'
    if imports:
        header += "\n" + "".join(f"{line}\n" for line in imports)
    return header + "\n" + "\n".join(funcs)


STATS_V1 = stats_py([], [MEAN, MEDIAN])
STATS_V2 = stats_py(["import math"], [MEAN, MEDIAN, STD_V1])
STATS_V3 = stats_py(["import math", "from collections import Counter"],
                    [MEAN, MEDIAN, STD_V1, MODE])
STATS_V4 = stats_py(["import math", "from collections import Counter"],
                    [MEAN, MEDIAN_BUGGY, STD_V1, MODE])
STATS_V5 = stats_py(["import math", "from collections import Counter"],
                    [MEAN, MEDIAN_BUGGY, STD_V1, MODE, RANGE])
STATS_V6 = stats_py(["import math", "from collections import Counter"],
                    [MEAN, MEDIAN_BUGGY, VARIANCE, STD_V2, MODE, RANGE])


# summarize.py -----------------------------------------------------------------

def summarize_py(names, rows, rounded=False):
    """Build summarize.py, printing one `label: expr` line per row."""
    width = max(len(label) for label, _ in rows) + 2
    lines = []
    for label, expr in rows:
        spec = ":.2f" if rounded and expr != "len(xs)" else ""
        lines.append(f'    print(f"{(label + ":").ljust(width)}{{{expr}{spec}}}")\n')
    return (
        '"""Print summary statistics for a file with one number per line."""\n'
        "\n"
        "import sys\n"
        "\n"
        f"from stats import {', '.join(names)}\n"
        "\n"
        "\n"
        "def main():\n"
        "    with open(sys.argv[1]) as f:\n"
        "        xs = [float(line) for line in f if line.strip()]\n"
        + "".join(lines)
        + "\n"
        "\n"
        'if __name__ == "__main__":\n'
        "    main()\n"
    )


ROWS_V1 = [("mean", "mean(xs)"), ("median", "median(xs)")]
ROWS_V2 = ROWS_V1 + [("std", "std(xs)")]
ROWS_V3 = [("count", "len(xs)"), ("min", "min(xs)"), ("max", "max(xs)")] + ROWS_V2
ROWS_V4 = ROWS_V3 + [("mode", "mode(xs)")]
ROWS_V5 = ROWS_V4 + [("range", "value_range(xs)")]

SUMMARIZE_V1 = summarize_py(["mean", "median"], ROWS_V1)
SUMMARIZE_V2 = summarize_py(["mean", "median", "std"], ROWS_V2)
SUMMARIZE_V3 = summarize_py(["mean", "median", "std"], ROWS_V3)
SUMMARIZE_V4 = summarize_py(["mean", "median", "mode", "std"], ROWS_V4)
SUMMARIZE_V5 = summarize_py(["mean", "median", "mode", "std"], ROWS_V4, rounded=True)
SUMMARIZE_V6 = summarize_py(["mean", "median", "mode", "std", "value_range"],
                            ROWS_V5, rounded=True)


COMMITS = [
    ("2026-10-05T09:12:00", "Initial commit",                 [("README.md", README_V1)]),
    ("2026-10-05T10:40:00", "Add mean and median",            [("stats.py", STATS_V1)]),
    ("2026-10-05T15:03:00", "Add summarize script",           [("summarize.py", SUMMARIZE_V1)]),
    ("2026-10-06T11:21:00", "Add exam scores data",           [("data/scores.txt", SCORES)]),
    ("2026-10-07T09:47:00", "Add standard deviation",         [("stats.py", STATS_V2),
                                                               ("summarize.py", SUMMARIZE_V2)]),
    ("2026-10-08T14:15:00", "Report count, min, and max",     [("summarize.py", SUMMARIZE_V3)]),
    ("2026-10-09T16:30:00", "Add mode",                       [("stats.py", STATS_V3),
                                                               ("summarize.py", SUMMARIZE_V4)]),
    ("2026-10-12T10:05:00", "Simplify median",                [("stats.py", STATS_V4)]),
    ("2026-10-12T13:48:00", "Round output to two decimals",   [("summarize.py", SUMMARIZE_V5)]),
    ("2026-10-13T09:30:00", "Add quiz scores data",           [("data/quiz.txt", QUIZ)]),
    ("2026-10-14T11:02:00", "Add range",                      [("stats.py", STATS_V5),
                                                               ("summarize.py", SUMMARIZE_V6)]),
    ("2026-10-15T15:55:00", "Document usage in README",       [("README.md", README_V2)]),
    ("2026-10-16T10:18:00", "Compute std from variance",      [("stats.py", STATS_V6)]),
    ("2026-10-16T17:40:00", "Ignore __pycache__",             [(".gitignore", GITIGNORE)]),
]


def git(args, cwd, env=None):
    subprocess.run(["git", *args], cwd=cwd, env=env, check=True)


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: 02-bisect-setup.py <path>")

    repo = Path(sys.argv[1]).expanduser().resolve()
    if repo.exists() and any(repo.iterdir()):
        sys.exit(f"error: {repo} exists and is not empty")
    repo.mkdir(parents=True, exist_ok=True)

    git(["init", "-q", "-b", "main"], cwd=repo)

    for date, message, writes in COMMITS:
        for relpath, content in writes:
            path = repo / relpath
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            git(["add", relpath], cwd=repo)

        env = {
            **os.environ,
            "GIT_AUTHOR_NAME":     AUTHOR_NAME,
            "GIT_AUTHOR_EMAIL":    AUTHOR_EMAIL,
            "GIT_COMMITTER_NAME":  AUTHOR_NAME,
            "GIT_COMMITTER_EMAIL": AUTHOR_EMAIL,
            "GIT_AUTHOR_DATE":     date,
            "GIT_COMMITTER_DATE":  date,
        }
        git(["commit", "-q", "-m", message], cwd=repo, env=env)

    print(f"created repo at {repo}")


if __name__ == "__main__":
    main()
