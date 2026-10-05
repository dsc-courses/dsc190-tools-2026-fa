# Editing files in the terminal

- How do you quit VIM?
    - **Answer**: Hit the escape key, type `:q` and press Enter.

- What does the `nano` command do?
    - **Answer**: Opens a simple text editor in the terminal.

- In nano, the bottom toolbar shows a shortcut like `^X Exit`. What key combination does `^X` refer to?
    - **Answer**: Ctrl-X.

# Globbing

- A directory contains the files `data_01.txt`, `data_02.txt`, and `data.txt`. If we run `rm data???.txt`, which files will be deleted?
    - **Answer**: `data_01.txt` and `data_02.txt` will be deleted, but not `data.txt`.

- A directory contains the files `.hidden_data.txt`, `data_02.txt`, and `data.txt`. If we run `rm *.txt`, which files will be deleted?
    - **Answer**: `data_02.txt` and `data.txt` will be deleted, but not `.hidden_data.txt` because globbing does not match hidden files by default.

- What does the command `cp *.csv backup/` do?
    - **Answer**: Copies anything in the current directory whose name ends in `.csv` into the `backup/` directory.

- Does the glob pattern `*.csv` recursively match CSV files in subdirectories of the current directory?
    - **Answer**: No — globbing is not recursive; it only matches files in the current directory.

- What happens when you run `cp *.txt data/` in a directory that contains no `.txt` files?
    - **Answer**: An error reporting that `*.txt` does not exist.

- What does `rm -rf *` do?
    - **Answer**: Recursively deletes everything in the current directory and below.

- What does `rm -r '*'` do? Notice the single quotes around `*`.
    - **Answer**: Deletes a single file named `*` if it exists, but does not perform glob expansion due to the quotes.

# Brace expansion

- What does `mkdir data_{1,2,3}` expand to?
    - **Answer**: `mkdir data_1 data_2 data_3`.

- What does `mkdir data_{a,b}{1,2,3}` expand to?
    - **Answer**: `mkdir data_a1 data_a2 data_a3 data_b1 data_b2 data_b3`.

# Variables

- What is the correct way to assign a string "Hello world!" to a variable named `greeting`?
    - **Answer**: `greeting="Hello world!"` or `greeting='Hello world!'` (with quotes to prevent word splitting).

- After setting `number=42`, how do you print the value of `number` using `echo`?
    - **Answer**: `echo $number`.

- After `x=42`, what does `echo $x + 1` print?
    - **Answer**: `42 + 1` — shell variables are just strings and there is no arithmetic.

# Quoting and expansion

- The current directory contains three files: `data1.csv`, `data2.csv`, and `data3.CSV`. How many arguments does `rm` receive in `rm *.csv`?
    - **Answer**: Two — `data1.csv` and `data2.csv` — because globbing is case-sensitive and does not match `data3.CSV`.

- The current directory contains three files: `data1.csv`, `data2.csv`, and `data3.CSV`. How many arguments does `rm` receive in `rm "*.csv"`?
    - **Answer**: One — the literal string `*.csv` — because quotes prevent glob expansion.

- The current directory contains three files: `data1.csv`, `data2.csv`, and `data3.CSV`. How many arguments does `rm` receive in `rm '*.csv'`?
    - **Answer**: One — the literal string `*.csv` — because single quotes also prevent glob expansion.

- The current directory contains three files: `data1.csv`, `data2.csv`, and `data3.CSV`. How many arguments does `rm` receive in `rm *.txt`?
    - **Answer**: One -- the literal string `*.txt` -- because there are no files matching the glob pattern, so it is not expanded.

- Suppose we set `x="foo bar baz"` and run `cd $x`. How many arguments does `cd` receive?
    - **Answer**: Three — `foo`, `bar`, and `baz` — because the variable is expanded and then word splitting occurs on the whitespace.

- A file is named "2026 report.txt" (with a space in the name). What command would you use to delete this file?
    - **Answer**: `rm "2026 report.txt"` or `rm '2026 report.txt'` (with quotes to prevent word splitting on the space).

- After setting `name=Justin`, what does `echo '$name'` print? Notice the quotes.
    - **Answer**: The literal string `$name` — single quotes prevent variable expansion.

- After setting `name=Justin`, what does `echo "$name"` print? Notice the quotes.
    - **Answer**: `Justin` — double quotes allow variable expansion.


# Command substitution

- What does `mkdir data_$(date +%Y-%m-%d)` do?
    - **Answer**: Creates a directory whose name is `data_` followed by today's date in `YYYY-MM-DD` format.

# I/O streams

- What three text streams does the shell connect to every program it runs?
    - **Answer**: Standard input (stdin), standard output (stdout), and standard error (stderr).

- What is the default source of standard input for a program run in the shell?
    - **Answer**: The keyboard.

- What is the default destination of standard output for a program run in the shell?
    - **Answer**: The terminal.

- What do you press to signal end-of-input to a program reading from stdin at the terminal?
    - **Answer**: Ctrl-D.

# Pipes

- What does the pipe operator `|` do in `ls -l | wc -l`?
    - **Answer**: Connects the stdout of `ls` to the stdin of `wc -l`, so `wc -l` counts the number of lines `ls` produced.

- What does `ls -l | wc -l` compute?
    - **Answer**: The number of files and directories listed by `ls` in the current directory.

- What does `ps aux | grep python` do?
    - **Answer**: Lists all running processes and then filters them to show only lines containing `python`.

- What does `find . -name "*.csv" | sort | less` do?
    - **Answer**: Recursively finds all CSV files under the current directory, sorts the list, and displays the sorted results in `less`.

# Redirection

- What does the `>` operator do in `find . -name '*.csv' > files.txt`?
    - **Answer**: Redirects stdout to `files.txt`, overwriting the file if it already exists.

- What does the `>>` operator do in `find . -name '*.py' >> files.txt`?
    - **Answer**: Redirects stdout to `files.txt`, appending to the file instead of overwriting it.

- In the command `find / -name test 2> errors.txt`, what does `2>` do?
    - **Answer**: Redirects stderr to the file `errors.txt`.

- In the command `find / -name test &> output.txt`, what does `&>` do?
    - **Answer**: Redirects both stdout and stderr to `output.txt`.
