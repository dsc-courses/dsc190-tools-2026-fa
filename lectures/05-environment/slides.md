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


Environments
============

To follow along:

1. In your terminal, run `cd dsc190-tools-2026-fa`
   and then `bash start-linux.sh`.
2. Inside the container, run `cd dsc190-tools-2026-fa` and then `git pull`.
3. Go to the first demo for Lecture 05:

```bash
demo 5 1
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Environment Variables</span>**

Variables
=========

Last time, we saw how to set and use shell variables:

```bash
name="Justin"
x=42

# prints: Hello Justin, your number is 42
echo "Hello $name, your number is $x."
```

Useful for *shell scripting*.

Variable Scope
==============

- Shell variables are only available in the **current** shell.
- They do **not** survive when you exit the shell.
- They are **not** "inherited".

```bash
name="Justin"
echo $name
# starts a new shell, *within* the old shell
bash
echo $name
# type <c-d> to exit the new shell
echo $name
```

Environment Variables
=====================

- <span class="term">**Environment variables**</span> are special: they **are** inherited.
- To define an environment variable, use the `export` command:

```bash
export name="Justin"
echo $name
bash
echo $name
```

Convention
==========

- By convention, environment variable names should be in all caps.

```bash
export NAME="Justin"
echo $NAME
bash
echo $NAME
```

Alternative: Inline Definition
==============================

- You can also define an environment variable inline when running a command:
- It will be local to that command's process.

```bash
NAME=Justin bash
echo $NAME
# press <c-d> to exit the new shell
# not defined
echo $NAME
```

<span class="exercise">**Exercise**</span>
===

Exported variables are inherited by child processes.

Are they also inherited by grandchild, great-grandchild, etc. processes? I.e.,
are they inherited recursively?

<!-- pause -->
**Yes!**

Environment Variables and Python
================================

- Any program run in a shell inherits its environment variables.
- In Python, you can access them via the `os` module:

```python
# in your python script...
import os
print(os.environ['NAME'])
```

Permanent Environment Variables
===============================

- Variables do not survive when you exit the shell.
- To make them permanent, you need to redefine them *every time* your shell starts.
- In `bash`, do this by editing the shell's startup file: `~/.bash_profile` (or `~/.profile` if that doesn't exist.)

```bash
# ~/.profile
...
export NAME="Justin"
```

<span class="exercise">**Exercise**</span>
===

Add an environment variable to your `~/.profile` that contains your name.

Then, exit your linux container and start it. Is `$NAME` still defined?

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">The PATH</span>**

Running Programs
================

- The shell's main job is to run programs.
- On Unix/Linux, a program is just a file marked as "executable".
- When you type a command, how does the shell know where to find it?

```bash
ls
```

The PATH
========

- The <span class="term">**$PATH**</span> environment variable contains a list of directories to search for programs.
```bash
echo $PATH

# prints:
# /usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
```

Note, $PATH is a single string, with directories separated by colons (`:`).

The PATH
========

- When you run a command, the shell looks through these directories to find an executable file with the same name.
- The *first* one it finds is the one it runs.


type
====

- The `type` command shows the program that is found by searching the $PATH.
- `type -a` shows all matches in the $PATH.

```bash
type grep
type python3
type cd
type ls
type -a ls
```

Permanently Modifying the PATH
==============================

- You'll often want to add directories to your $PATH, e.g., to run programs you installed yourself.
- To do so, edit `~/.profile`.
- Example: add `~/bin` to the $PATH:

```bash
# ~/.profile
...
export PATH="~/bin:$PATH"
```

Order Matters!
==============

- The first entries in the $PATH are searched first.
- To give a directory **high priority**, put it at the beginning:
```bash
export PATH="~/bin:$PATH"
```
- To give a directory **low priority**, put it at the end:
```bash
export PATH="$PATH:~/bin"
```

---


<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Python Environments</span>**

Python Environments
===================

- Suppose we write a Python program that uses a package (like `numpy` or `pandas`).
- Python packages are also just files (and directories).
- How does Python find the package?

```python
import numpy
import pandas
```

Python's Search Path
====================

- Python looks for packages in the directories listed in the `sys.path` variable.

```python
# in your python script...
import sys
print(sys.path)
```

<span class="exercise">**Exercise: demo 5 1**</span>
===

`print_path.py` prints the directories in `sys.path`. What are they?

`sys.path`
==========

- The first entry: directory of the script being run.
    - This is what enables importing "helper" files.
- `/usr/lib/python3.11`: python standard library.
- `/usr/lib/python3/dist-packages`: "system" packages

Checking a Package's Location
=============================

- To check where a package is being imported from, look at its `__path__` attribute:

```python
import numpy
print(numpy.__path__)
```

Modifying the Search Path
=========================

To modify the package search path, set the `sys.path` variable in your script:

```python
# in my_script.py
import sys
sys.path.append('/path/to/my/packages')
```

Alternative: PYTHONPATH
=======================

You can also set the `PYTHONPATH` environment variable:

```bash
# in the shell
export PYTHONPATH="/path/to/my/packages:$PYTHONPATH"
python3 my_script.py
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Executables and Shebang Lines</span>**

---

Customizing Your Tools
======================

- Let's say you've written a Python script, `myscript.py`.
- You can run it with `python myscript.py`.
- But you want to be able to run it from anywhere (just like `ls`, `grep`, etc.) without typing `python` first.
- Can do this by:
    1. Adding a "shebang line" to the file.
    2. Marking it as executable.
    3. Adding its directory to the $PATH.

Step 1: Add a Shebang Line
==========================

- If the first line of a file starts with `#!`, the shell treats it as a <span class="term">**shebang**</span>.
- Immediately after `#!` should be the path to a *interpreter* (like Python, bash, etc.)
- In our case, we want to use Python 3:

```python
#!/usr/bin/python3
print("Hello, world!")
```

Step 1: Add a Shebang Line (Cont.)
===================================

- Instead of hardcoding the path to Python, we can use `env` to find it for us:

```python
#!/usr/bin/env python3
print("Hello, world!")
```

Step 2: Mark as Executable
==========================

- Our file is currently just treated as text.
- To mark it as executable, use the `chmod` command with `+x`:

```bash
chmod +x myscript.py
```

- Aside: `chmod` is also used to set file permissions (read, write, execute).


Running the Script
==================

- Now we can run the script directly without typing `python`.
- In the shell:

```bash
./myscript.py
```

- The `./` is necessary because the current directory is not in the $PATH.

Renaming the Script
===================

- In fact, we can get rid of the `.py` extension, since the shebang line tells the shell how to run it:

```bash
mv myscript.py myscript
./myscript
```

Step 3: Add to the PATH
=======================

- To make the script runnable from anywhere, add its directory to the $PATH.
    - You might want to do this in `~/.bash_profile` so it is permanent.

```bash
export PATH="$(pwd):$PATH"
cd somewhere/else
myscript
```

Customizing Your Tools
======================

- This is an example of *customizing your tools*.
- Idea:
    - Have an annoying task you do often? (e.g., check the surf report)
    - Have an agent write a script and add it to your $PATH.
