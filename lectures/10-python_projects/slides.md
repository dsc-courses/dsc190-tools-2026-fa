---
theme:
  path: ../../.presenterm/theme.yaml
  override:
    footer:
      style: template
      right: "{current_slide} / {total_slides}"
options:
  list_item_newlines: 2
---


Python Project Tooling
======================

To follow along, open a terminal on your own machine (macOS, or WSL on
Windows) and `cd` to a place where you want to work.

You should not use the Docker container.

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Python Project Tooling</span>**

Python Project Management
=========================

- Our language of choice is Python.
- Now: tools for managing Python projects.

uv
==

- `uv` is a Python project manager.
- It replaces `pip` and `python -m venv`
- It is faster, has more features, and is *declarative*.

Installing uv
=============

On macOS with Homebrew:

```bash
brew install uv
```

On Ubuntu in Windows WSL:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


uv init
=======

- To start a new python project, run:

```bash
uv init <project_name>
```

uv init
=======

`uv init` creates a basic project structure:

```bash
 .
├──  .git
├──  .gitignore
├──  .python-version
├──  main.py
├──  pyproject.toml
└──  README.md
```

uv init for packages
====================

- By default, uv init creates a structure for an *app*.
- If you're building a package, you can use the `--package` flag:

```bash
uv init --package <project_name>
```

```bash
 .
├──  .git
├── 󱧼 src
│   └──  project_name
├──  .gitignore
├──  .python-version
├──  pyproject.toml
└──  README.md
```

pyproject.toml
==============

- `pyproject.toml` contains *metadata* about the project, including:
    - The project name and version.
    - The dependencies.
    - The Python version.

```toml
[project]
name = "project_name"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.14"
dependencies = []
```

Adding Dependencies
===================

- uv's main job is to manage dependencies.
- To add a dependency (e.g., numpy), run:
```bash
uv add numpy
```
- Notice that this updates `pyproject.toml`:
```toml
# ...
dependencies = [
    "numpy>=2.4.4",
]
```

Specifying Versions
===================

- By default, uv adds the latest version of a package.
- You can specify a version (or version range) using the same syntax as pip:

```bash
uv add "numpy==2.4.4" # exactly version 2.4.4
uv add "numpy>=2.0.0" # any version newer than 2.0.0
uv add "numpy<=2.4.4" # any version older than 2.4.4
uv add "numpy>2.0.0,<=2.4.4" # any version between 2.0.0 and 2.4.4 
uv add "numpy~=2.4"   # any version compatible with 2.4 (i.e., 2.4.x)
```

Virtual Environments
====================

- When "uv add" was run, it created a *virtual environment* in .venv/
- But it does not *activate* the venv.
    - It doesn't modify the path.
- To activate it, either:
    - Run "`uv run bash`" (or fish, zsh, etc.) to open a new shell.
    - Or, "source .venv/bin/activate" (or .venv/bin/activate.fish, etc.) 

uv run
======

- uv provides a shortcut for running commands in the venv *without* needing to activate them:

```bash
uv run <command>
```

- Can also provide a script name:

```bash
uv run main.py # equivalent to "uv run python main.py"
```

Demo
====

Update main.py to import numpy and print its path. Then:

1. Try running the script outside of the venv.
2. Try running it with `uv run main.py`.

(Make sure you've added numpy as a dependency first!)

Adding Dependencies via pyproject.toml
======================================

- You can also add dependencies by editing `pyproject.toml` directly.
- After editing, run "uv sync" to synchronize the venv with the pyproject.toml file:


Example
=======

Install pandas into the project by adding it to `pyproject.toml` and running "uv sync".

Declarative vs. Imperative
=========================

- The old way of managing dependencies (e.g., with pip) is *imperative*:
    - You run commands that change the state of the environment.
    - It can be hard to keep track of what you've done, and to reproduce it on another machine.
- The new way (with uv) is *declarative*:
    - You declare the desired state of the environment (in pyproject.toml).
    - The tool takes care of making the environment match that state.
- <span class="good">**Declarative > Imperative**</span>

uv add, again
=============

- "uv add" is a shortcut for:
    1. Adding the dependency to pyproject.toml.
    2. Running "uv sync" to update the venv.


uv.lock
=======

- When "uv add" is run, it creates/updates a <span class="term">**lockfile**</span> named `uv.lock`.
- This file lists every dependency and its exact version that was installed in the venv.
- But also, every dependency of every dependency, and so on (i.e., the entire "dependency tree").
- "uv sync" uses the lockfile to ensure that the exact same versions are installed in the venv.

uv.lock and Collaboration
=========================

- The lockfile ensures that everyone on the team is using the *exact same* versions of every package.
- It should be committed to version control.
- To start working on the project:
    1. Clone the repo.
    2. Run "uv sync" to create a venv with the exact same dependencies as everyone else.

Removing and Upgrading Deps
===========================

- To remove a dependency, run:

```bash
uv remove <package_name>
```

- To upgrade a dependency to the latest version, run:

```bash
uv lock --upgrade-package <package_name>
```

- To upgrade all dependencies to their latest versions, run:

```bash
uv lock --upgrade
```



Dev Dependencies
================

- Sometimes, you want to install a dependency that is only needed for development. 
    - Example: "ruff" (a python *formatter* and *linter*).
- These should be kept separate from the "runtime" dependencies.
- Add them with the `--dev` flag:

```bash
uv add --dev ruff
```

Dev Dependencies in pyproject.toml
==================================

- Dev dependencies are stored in a separate section of pyproject.toml:

```toml
# ...
dependencies = [
    "numpy>=2.0.0,<2.4",
    "pandas"
]

[dependency-groups]
dev = [
    "ruff>=0.15.12",
]
```


Managing the Python Version
===========================

- Sometimes your project requires a specific version of Python.
- First, specify required version in pyproject.toml:

```toml
# ...
requires-python = ">=3.10,<3.13"
```
- Run "`uv python pin <version>`" to set the Python version that will be used in the venv:

```bash
uv python pin 3.11
```

Summary
=======

- uv is the modern way to manage Python project dependencies.
- Use it instead of "pip" and "python -m venv".
- We've only covered some of its features, but it has many more (e.g., publishing packages to PyPI).

A Useful Trick
==============

- We've seen how to make a *shell script* with Python:

```python
#! /usr/bin/env python3

import numpy as np
import sys

numbers = [float(x) for x in sys.argv[1:]]
print(np.mean(numbers))
```

Save it as mean.py, then run:
```bash
$ ./mean.py 1 2 3 4
2.5
```

<span class="bad">**Problem**</span>
===

- This script only works if you have numpy installed in your global Python environment.
- uv provides a nice solution.
    - You can specify dependencies *within the script
      itself*.
    - See: https://docs.astral.sh/uv/guides/scripts/

A Useful Trick
==============

```python
#! /usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy"]
# ///
import numpy as np
import sys

numbers = [float(x) for x in sys.argv[1:]]
print(np.mean(numbers))
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Python Dev Tools</span>**

Dev Tools
=========

- There are many tools that help you write better code.
    - *Linters* check your code for potential errors and style issues.
    - *Formatters* automatically format your code according to a style guide.
    - *Type checkers* check your code for type errors.
    - *Testing frameworks* run tests to check correctness.

Irony
=====

- These tools have always been crucial for writing good code.
- But they are even more important now with AI coding agents.
- These tools keep the AI *on track* by providing automatic feedback.

Our Tools
=========

We will cover:

- ruff: linter/formatter
- mypy: type checker
- pytest: testing framework

ruff
====

- Ruff is a linter *and* formatter.
- It checks for common errors and makes sure your code is tidy.
- To install it into your project with uv:

```bash
uv add --dev ruff
```
- To run it anywhere (outside of a project) with uv:

```bash
uvx ruff
```

Example
=======

```python
import pandas
import numpy as np

arr = [1, 2, 3, 4]; print(np.mean(arr))
```

Example
=======

Use "`ruff check <file>`" to see the errors:

```bash
F401 [*] `pandas` imported but unused
 --> main.py:1:8
  |
1 | import pandas
  |        ^^^^^^
2 | import numpy as np
  |
help: Remove unused import: `pandas`

E702 Multiple statements on one line (semicolon)
 --> main.py:4:19
  |
2 | import numpy as np
3 |
4 | arr = [1, 2, 3, 4]; print(np.mean(arr))
  |                   ^
  |

Found 2 errors.
[*] 1 fixable with the `--fix` option.
```

Fixing Errors
=============


- Use "`ruff check --fix <file>`" to automatically fix the error.
- Some errors must be fixed manually.

PEP8
====

- PEP8 is the official Python style guide.
- It says things like:
    - Use 4 spaces for indentation.
    - Limit lines to 79 characters.
    - Use snake_case for variable and function names.
- Ruff doesn't check all PEP8 rules, but it checks many of the most important ones.

Formatting
==========

- Ruff can also automatically format your code.
```bash
ruff format <file>
```

Formatting
==========

Before:
``` python
x=2+3
result = some_function(argument_one,argument_two,argument_three,argument_four,argument_five,argument_six)
```

After:
```python
x = 2 + 3
result = some_function(
    argument_one,
    argument_two,
    argument_three,
    argument_four,
    argument_five,
    argument_six,
)
```



