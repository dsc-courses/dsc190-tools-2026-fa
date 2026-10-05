# Assignment 02: Shell Scripting

**Due**: Tuesday, October 13 at 11:59 PM on Gradescope

## Getting Started

In your terminal, run `cd dsc190-tools-2026-fa` and then `bash start-linux.sh`.
Inside the container, run `cd dsc190-tools-2026-fa` and then `git pull`. Then
`cd` into `assignments/02-shell/`.

Then, run `python setup.py`. This will generate the sample data for this
assignment. If you ever want to get a fresh copy of the data, simply delete the
`data/` directory and run `python setup.py` again.

## Part 1) Basic shell scripting

### Background

In lecture, we saw that the shell's main job is to run programs and manipulate
files. As a user, you typically do this *interactively*, by running commands.
However, you can also write these commands into a file, called a *shell
script*. By running the shell script, you can execute all the commands in it at
once. This is a great way to automate repetitive tasks.

To write a shell script, simply create a new file (usually, though not
necessarily, with a `.sh` extension) and write your commands in it, with one
command per line. For example, here is a shell script that prints the number of
CSV files in or below the current directory:

```bash
# count_csv.sh
n=$(find . -name "*.csv" | wc -l)
echo "There are $n CSV files."
```

A `#` at the beginning of a line indicates a comment, which is ignored by the
shell.

To run this script, you can use the `bash` command:

```bash
bash count_csv.sh
```

Note that when you run a script, it executes within the current directory of
your shell, which is not necessarily the same directory where the script lives.
If you wanted to run the script from a different directory, you would need to
`cd` to that directory within the script.

### The Task

Suppose you're working on a project that requires you to do a certain analysis
every day. Every time you run the analysis, you must create the following
directory structure:

```text
analysis-YYYY-MM-DD/
    README.md
    data/
        raw/
        processed/
    results/
```

That is, you need to create a directory called `analysis-YYYY-MM-DD`, where `YYYY-MM-DD` is replaced by the current date. Inside that directory, you need to create a `README.md` file, and two subdirectories: `data/` and `results/`. Inside `data/`, you need to create two more subdirectories: `raw/` and `processed/`.

Moreover, the `README.md` file needs to contain the following text:

```text
# Analysis for YYYY-MM-DD

```

Where `YYYY-MM-DD` is again replaced by the current date.

Write a simple shell script named `setup_analysis.sh` that automates this
process. When you run the script, it should create the directory structure
within the same directory as the script, and populate the `README.md` file with
the correct content. Include `setup_analysis.sh` as one of the files in your
Gradescope submission.

### Hints

Remember the `date` and `echo` commands from lecture. Also, remember that you
can redirect the output of a command into a file using `>`. That will be useful
for creating the `README.md` file.

## Part 2) Shell scripts with arguments

### Background

Shell scripts can also take *arguments* -- values that are passed to the script
when you run it. The first argument is accessed within the script as `$1`, the second as `$2`, and so on.

For example, this script takes two files names as arguments and "swaps" their
filenames.

```bash
# swap.sh
mv "$1" temp_swap_file
mv "$2" "$1"
mv temp_swap_file "$2"
```

When called as:

```bash
bash swap.sh foo.txt bar.txt
```
it will rename `foo.txt` to `bar.txt` and `bar.txt` to `foo.txt`.

### The Task

Write a shell script named `backup.sh`. It should take a single argument: a
pattern that is passed to `find`. The script should find all files in the
current directory (and its subdirectories) that match the pattern (insensitive
to case), and copy them to a "backup" version, which is the same file name with
`.bak.YYYY-MM-DD` appended to it.

For example, if a directory contains the files:

```text
data.csv
results.CSV
report.txt
```

and you run the script (on October 7, 2026):

```bash
bash backup.sh '*.csv'
```

the directory should now contain the following files:

```text
data.csv
data.csv.bak.2026-10-07
results.CSV
results.CSV.bak.2026-10-07
report.txt
```

Include this script in your Gradescope submission as well.

**Hint**: there is a straightforward way of doing this that results in your
script containing just a single line. Try using command substitution.

## Part 3) A more complex script

### Background

Shell scripts can be quite powerful. They can include `for`-loops,
`if`-statements, string manipulation, and more. However, the syntax for these
is notoriously arcane and confusing, and so we advise you to **avoid** complex
shell scripts whenever possible. If you find yourself needing to write a
complex script, it's often better to write it in Python instead -- as we'll see
in a moment.

To get a sense of what a more complex shell script looks like (hopefully
dissuading you from trying to write them!) without having to write one ourselves,
we will ask the coding agent in `opencode` to write one for us.

When you ran `python setup.py`, it created a directory called
`data/temperatures/`. This directory contains CSV files with temperature
readings from various weather stations. The files are named like:

```text
<station>_temperature_<date>.csv
```

where `<station>` is a station name (like `san_diego` or `santa_barbara`) and
`<date>` is a date. Unfortunately, the dates are messy: some use `YYYY-MM-DD`
format (e.g., `2025-01-07`), while others use `MM-DD-YYYY` format (e.g.,
`01-07-2025`). On top of that, some dates are missing leading zeros (e.g.,
`2025-1-7` or `1-7-2025`).

### The Task

Your task is to write a shell script called `rename_temperatures.sh` that takes
in one argument (the path to the directory containing the temperature files)
and renames every file in that directory so that the date is in `YYYY-MM-DD`
format with leading zeros. For example:

- `san_diego_temperature_3-9-2025.csv` should become `san_diego_temperature_2025-03-09.csv`
- `fresno_temperature_2025-2-28.csv` should become `fresno_temperature_2025-02-28.csv`
- `oakland_temperature_2025-01-28.csv` should stay the same (it's already correct).

You can tell which format a date is in by looking at whether the year (a
four-digit number) comes first or last.

Don't write this script by hand -- we do not know enough about shell scripting
to do it correctly! Instead, use the coding agent in `opencode` to generate
this script. Open `opencode` in the terminal, describe the problem, and ask it
to write the script for you. You can even direct it to this README file. It
will be difficult to tell by reading the generated code whether it works
correctly, so make sure to have the agent test its code on the actual files in
`data/temperatures/` and verify that it works. You may need to iterate on the
prompt a few times to get it right.

Once you are satisfied, save the script as `rename_temperatures.sh` and include
it in your Gradescope submission.

**Note**: running shell scripts that you don't understand is, in general, a
*bad idea*™. Shell scripts can do anything that you can do in the terminal,
including deleting files. Shell scripts with bugs or malicious intent can cause
a lot of damage. In this case, however, it's OK: you're running these scripts
in a docker container that is isolated from your main machine, and so the
possible damage is limited to the files in this container.

## Part 4) Scripting with Python

### Background

Take another look at the shell script that you wrote/generated in the previous
part. Chances are, it looks pretty complicated and is difficult to understand.
It probably uses many shell features that we did not discuss in lecture. In
fact, it likely uses shell features that most programmers are unfamiliar with.
This is a common problem with shell scripts -- shell scripting is a powerful
tool, but its syntax for things like string manipulation and loops is *not*
very user-friendly and hard to remember.

Nowadays, there are much better tools for writing scripts that automate tasks,
and you already know one of them: Python. In fact, Python originated as a
"scripting" language, and an alternative to shell scripting. A common piece of
advice (and one that we endorse) is: if you find yourself needing to write more
than the simplest loop, conditional, or string manipulation in a shell script,
you should probably be writing a Python script instead.

Python provides many built-in libraries for working with files and running
commands. Some that you might find useful are:

- `pathlib`: for working with file paths, renaming files, etc.
- `subprocess`: for running shell commands from Python.
- `os`: for listing files in a directory, working with paths, etc.
- `sys`: for accessing command-line arguments, etc.

In particular, you can run shell commands from within Python using the
`subprocess` library. This is called "shelling out" -- you can write most of
your logic in Python, and then call out to the shell to run specific commands
when needed, getting the best of both worlds.

For example:

```python
import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)
```

This runs the command `ls -l` and captures its output. The `capture_output=True`
argument tells Python to capture the command's output instead of printing it
to the terminal, and `text=True` tells Python to return the output as a
string (rather than raw bytes).

Two useful keyword arguments:

- `cwd`: sets the working directory for the command. For example,
  `subprocess.run(["ls"], cwd="/tmp")` runs `ls` inside `/tmp`.
- `shell=True`: allows you to pass the command as a single string instead of a
   list, and have it interpreted by the shell. For example,
   `subprocess.run("ls *.csv", shell=True)` uses the shell to expand the
   `*.csv` glob. Without `shell=True`, you must pass the command as a list of
   strings (e.g., `["ls", "-l"]`).

### The Task

Write a Python script called `rename_temperatures.py` that does the same thing
as your `rename_temperatures.sh` from Part 3: it should take a directory path
as a command-line argument and rename all of the temperature files in that
directory so that their dates are in `YYYY-MM-DD` format with leading zeros.

Your script should use `subprocess.run` to call `mv` to rename each file. The
rest of the logic -- listing the files, parsing the filenames, deciding on the
new name -- should be done in Python, however you'd like.

You may use `opencode` to generate this script (in fact, you're encourage to do
so). Either way, make sure to test it on the actual files in `data/temperatures/` and verify that it works as expected.

## Part 5) Python and STDIN

### Background

In lecture, we saw that the shell connects each program to three text streams:
STDIN, STDOUT, and STDERR. This is true for every program, including python
scripts that you write.

To read from STDIN in a python script, you can use `sys.stdin`. This "virtual
file" behaves like any other file object in Python, and you can read from it
using the familiar methods. For example, this script reads lines from STDIN and prints them in uppercase:

```python
import sys

for line in sys.stdin:
    print(line.upper(), end="")
```

You can run this script and provide input through the terminal:

```bash
# prints "HELLO WORLD"
echo "hello world" | python uppercase.py
```
### The Task

Write (or generate) a python script called `filter_malformed_dates.py` that
reads lines from STDIN, where each line is a filename in the same format as the
temperature files (e.g., `san_diego_temperature_3-9-2025.csv`). The script
should print out the filenames whose dates are *not* in YYYY-MM-DD format, one
per line.

Your script should work when run in a command like:

```bash
find data/temperatures/ -name "*.csv" | python filter_malformed_dates.py
```

The result of this command should be each malformed filename printed on its own
line.

## What to Submit

You will submit multiple files to Gradescope. They are:

- `setup_analysis.sh`: the shell script from Part 1.
- `backup.sh`: the shell script from Part 2.
- `rename_temperatures.sh`: the shell script from Part 3.
- `rename_temperatures.py`: the python script from Part 4.
- `filter_malformed_dates.py`: the python script from Part 5.

### Getting your files out of the container

Chances are, you wrote/generated these scripts within your Docker container (at
least, that was the expected workflow). In order to submit these files, you
will need to get them out of the container and onto your main machine. The easiest
way to do this for now is to open a shell (on your main machine, *not* in the container! On Windows, use the Ubuntu app) and run the following commands. First, run:

```bash
docker ps
```

This will print out all of the docker containers that are currently running. Find
the one for this course (look at the "name" column), and then note the first few
characters of its "CONTAINER ID" (for example, "22a2d"). Then, run:

```bash
docker cp <container_id>:/home/student/<path-to-file> .
```

Here, replace `<container_id>` with the container ID you noted (e.g., "22a2d"),
and replace `<path-to-file>` with the path to the file you want to copy,
relative to the home directory in the container. For example, if you wrote `setup_analysis.sh` in the `assignments/02-shell/` directory within the course repo,
and your container ID is "22a2d", you would run:

```bash
docker cp 22a2d:/home/student/dsc190-tools-2026-fa/assignments/02-shell/setup_analysis.sh .
```

This will copy the file from the container to your current directory on your
main machine. You can repeat this process for each of the files you need to
submit. Once you have all the files on your main machine, you can submit them
to Gradescope.

### Grading

As with the first assignment, all of the tests for this assignment are *public*
tests. So the score that you see upon submitting your code to Gradescope is the
score you will get on this assignment. You can submit as many times as you
like, and your score will update each time.
