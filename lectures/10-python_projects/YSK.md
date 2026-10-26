# uv basics

- What two older Python tools does `uv` replace?
    - **Answer**: `pip` and `python -m venv`.

- Which file does `uv init` create to hold a project's metadata and dependencies?
    - **Answer**: `pyproject.toml`.

- What command adds `numpy` as a dependency to a uv project?
    - **Answer**: `uv add numpy`.

- What does the command `uv add "numpy==2.4.4"` do?
    - **Answer**: Adds numpy pinned to exactly version 2.4.4.

- What command removes `numpy` from a uv project?
    - **Answer**: `uv remove numpy`.

- What command upgrades only `numpy` to its latest allowed version?
    - **Answer**: `uv lock --upgrade-package numpy`.

- What command upgrades all dependencies in a uv project to their latest allowed versions?
    - **Answer**: `uv lock --upgrade`.

# Virtual environments and uv run

- What command activates a uv project's virtual environment in a bash shell?
    - **Answer**: `source .venv/bin/activate`.

- What does `uv run pytest` do?
    - **Answer**: Runs `pytest` inside the project's virtual environment.

- What does `uvx ruff` do?
    - **Answer**: Installs and runs `ruff` outside of a project.

# Declarative dependency management

- What does `uv sync` do?
    - **Answer**: Updates the virtual environment to match the dependencies declared in `pyproject.toml` and `uv.lock`.

- What is the purpose of the `uv.lock` file?
    - **Answer**: It records the exact version of every installed package (and every recursive dependency) so the environment can be reproduced.

- After cloning a uv project from GitHub, what single command sets up an identical virtual environment?
    - **Answer**: `uv sync`.

# Dev dependencies

- What is a "dev dependency"?
    - **Answer**: A package needed only during development (e.g., a linter or test runner), not at runtime.

- What command adds `ruff` as a dev dependency?
    - **Answer**: `uv add --dev ruff`.

# Dev tools: linters, formatters, type checkers, tests

- What does a *linter* do?
    - **Answer**: Checks code for potential errors and style issues.

- What command uses ruff to check `main.py` for lint errors?
    - **Answer**: `ruff check main.py`.

- What command uses ruff to automatically fix the lint errors it finds in `main.py`?
    - **Answer**: `ruff check --fix main.py`.

- What command uses ruff to reformat `main.py` according to its style rules?
    - **Answer**: `ruff format main.py`.

- What is PEP8?
    - **Answer**: The official Python style guide.

- According to PEP8, what naming convention should be used for variable and function names?
    - **Answer**: `snake_case`.
