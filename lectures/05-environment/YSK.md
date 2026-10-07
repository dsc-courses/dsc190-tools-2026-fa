# Environment variables

- You set `name="Justin"` and start a new shell with `bash`. What does `echo $name` print?
    - **Answer**: Nothing — shell variables are not inherited by child processes.

- You run `export name="Justin"` and start a new shell with `bash`. What does `echo $name` print?
    - **Answer**: `Justin` — exported variables are inherited by child processes.

- What command turns a shell variable into an environment variable?
    - **Answer**: `export`

- After `export NAME="Justin"`, which processes inherit `$NAME`?
    - **Answer**: All descendant processes (children, grandchildren, etc.).

- In `NAME=Justin bash`, what is the scope of `NAME`?
    - **Answer**: Only the `bash` child process, not the current shell.

- What does `echo $NAME` print if `NAME` has never been set?
    - **Answer**: Nothing (undefined variables expand to empty strings).

- By convention, how should environment variable names be written?
    - **Answer**: In all uppercase (e.g., `NAME`, `PATH`).

- How do you access environment variable `NAME` in Python?
    - **Answer**: `os.environ['NAME']` (after `import os`).

- In Bash, where do you define an environment variable so it persists across shell sessions?
    - **Answer**: In `~/.profile` (or `~/.bash_profile`).

# The PATH

- What character separates directories in `$PATH`?
    - **Answer**: A colon (`:`).

- If `PATH="/usr/local/bin:/usr/bin:/bin"` and `ls` exists in all three directories, which copy runs when you type `ls`?
    - **Answer**: `/usr/local/bin/ls`

- What does `type grep` show?
    - **Answer**: The path of the executable found via `$PATH`.

- What does `type -a grep` show?
    - **Answer**: All matching executables for `grep` across all `$PATH` directories.

- If `PATH="/usr/bin:/bin"` and you run `export PATH="~/bin"` (without including `$PATH`), what is the new value of `$PATH`?
    - **Answer**: `~/bin`

- If `PATH="/usr/bin:/bin"` and you run `export PATH="~/bin:$PATH"`, what is `$PATH` now?
    - **Answer**: `~/bin:/usr/bin:/bin`

- Where should you put `export PATH="~/bin:$PATH"` so it persists?
    - **Answer**: In `~/.profile` (or `~/.bash_profile`).

- What happens if you run `export PATH=""` (to empty the PATH) and then run `grep`?
    - **Answer**: You get a "command not found" error

# Python's search path

- What variable holds the list of directories Python searches on `import`?
    - **Answer**: `sys.path`.

- What does `python -c 'import sys; print(sys.path)'` print?
    - **Answer**: The list of directories Python searches on `import`.

- What is typically the first entry in `sys.path`?
    - **Answer**: The directory containing the script being run.

- How do you find where `numpy` is installed on disk?
    - **Answer**: `import numpy` and print `numpy.__path__`.

# Modifying Python's search path

- What does `sys.path.append('/path/to/my/packages')` do?
    - **Answer**: Adds a directory to Python's search path so packages there can be imported.

- Which environment variable can be modified to contain additional directories for Python to search for packages?
    - **Answer**: `PYTHONPATH`.
