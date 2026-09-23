# Demo 01: Cleaning Up a Messy Project

A collaborator has dumped a bunch of files into this project directory with
no organization. Your job is to clean it up using only the command line.

## Step 1: Look around

- Use `ls -a` to reveal hidden files.
- Use `ls -l` to see file sizes and dates.
- Flags can be combined: `ls -al` or `ls -la`.

- **Question**: How many files are in the directory? Don't count directories.

## Step 2: Peek inside a file

- Use `less data_FINAL_v2.csv` to view the largest data file.
    - Scroll (slowly) with arrow keys or (or `j` and `k`).
    - Scroll faster with `Ctrl-d` (down) and `Ctrl-u` (up).
    - Jump to the end with `G` and back to the top with `g`.
    - Use `/` to search. `n` goes to next match, `p` to previous.
    - Press `q` to quit.

**Question**: What name is in the last line of the file?
**Question**: What region is associated with "Justin"?

## Step 3: Get help

- Most commands have a `-h` or `--help` flag that shows usage information.
- You can also use `man <command>` to read the manual page for a command.
    - Works the same as `less`.
- `tldr` gives concise usage examples for common commands.
    - It isn't installed everywhere!

**Task**: how do you get `ls` to use colors?

## Step 4: Explore the nested directories

- Use `cd` without a directory name to go to your home directory.
- Use `cd -` to jump back to your previous directory.
- Use `cd ..` to go up one level.
- Use `pwd` to see your current directory.

**Task** `cd` to your home directory, and then get back to the demo without using `cd -`.
**Task**: `cd` down into the `raw/` directory to see the survey data looks like, then go back up to the main demo directory.

## Step 5: Create an organized folder structure

- Use `mkdir` to create new directories.
    - Accepts multiple directory names at once.
    - `mkdir -p foo/bar/baz` creates nested directories in one command.

**Task**: use `mkdir` to create three new directories in the project root: `scripts/`, `figures/`, and `data/`.

## Step 6: Move files into the right places

- `mv <source> <destination>` moves a file or directory from the source path to the
  destination path.
- You can provide multiple source paths to move multiple files into the same destination directory.
- There's also "globbing", which we'll talk about in a future lecture.

**Task**: Move the Python scripts into `scripts/`.
**Task**: Move the plot images into `figures/`.
**Task**: Move the CSV data files and the raw data into `data/`.

## Step 7: Rename and copy files

- `mv <old-name> <new-name>` can also be used to rename files.
- `cp <source> <destination>` copies files instead of moving them.
    - The `-r` flag can be used to copy directories and their contents recursively.

**Task**: Rename `data_FINAL_v2.csv` to `cleaned-data.csv`.
**Task**: Make a backup copy of `results.csv`: `cp results.csv results.bak.csv`
**Task**: Copy the `scripts/` directory to your home directory.

## Step 8: Delete junk files

- `rm` deletes files, and `rm -r` deletes directories and their contents.
- `rm -rf` deletes directories and their contents without prompting for
  confirmation.
- Be VERY CAREFUL! There is no "undo" for `rm`.

**Task**: Remove the temp file.
**Task**: Remove the hidden `.DS_Store`.
**Task**: Remove the entire `scratch/` directory.
**Task**: Delete the `scripts/` directory you copied to your home directory
