---
theme:
  path: ../../.presenterm/theme.yaml
options:
  list_item_newlines: 2
---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Lecture 03 — find and grep</span>**

`find` and `grep`
=================

To follow along:

1. Run `bash start-linux.sh`.
2. `cd` into the course repository directory.
3. Run `git pull`.
4. Go to the first demo for Lecture 03:

```bash
demo 3 1
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Agents</span>**

AI
==

- Since the release of ChatGPT in late 2022, it's been clear that AI will be a tool in our toolset.
- But it's only been recently -- with the release of Claude Code in early 2025 -- that AI has become **the** tool.


LLMs
====

- ChatGPT is an interface to a large language model (LLM).
- LLMs are "next word predictors" that have been trained on huge amounts of text.
    - When asked a question, they produce text that is "reasonable".
    - This is why they "hallucinate".
- By themselves, LLMs cannot interact with the outside world.


Example
=======

- How many "r"'s are in the word "strawberry"?
- "LLM's can't count"

Agents
======

- An **agent** is an LLM that:
    - has access to the outside world via **tools**,
    - and can call those tools in a loop.
- Example: an LLM that can run commands in the Unix shell, see the output, and react accordingly.
- While not the first, *Claude Code* was to agents as ChatGPT was to LLMs.

Ground Truth
============

- By making tool calls, agents can get "ground truth" about the world.
- Example: number of "r"'s in "strawberry":
    - An LLM makes a reasonable guess: "There are 2 'r's in 'strawberry'".
    - An agent writes reasonable Python code to count the "r"'s, runs it, and sees that the answer is 3.

Try it out...
=============

- Your docker container has *opencode* pre-installed.
- opencode is a coding agent that works in the terminal.
- Let's try it out.

Getting Help in the Shell
=========================


- 1976: `man <command>` or `<command> --help`
- 2016: `tldr <command>`
- 2026: AI

Try:
```bash
ask "How do I use the ls command?"
ask "Why didn't that last command work?"
```
---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">find</span>**

The `find` Command
==================

- We can use the *find* command to *recursively* search for files or directories.

Finding by Name
===============


```bash
find <root-of-search> -name '<pattern>'
```

Examples:

```bash
# find anything named "README.md" in this directory
# or any subdirectory, recursively
find . -name 'README.md'

# find anything named README.md under logs/
find logs/ -name 'README.md'
```

<span class="exercise">**Exercise: demo 3 1**</span>
===

Find anything named "README.md" in the demo.

How many are there?



Finding by Name: Wildcards
==========================

- By default, `-name` looks for *exact* matches.
- Use * as a wildcard to match any characters.
- The quotes are important!

```bash
# find all CSV files under the current directory
find . -name '*.csv'

# find anything that starts with "test"
find . -name 'test*'
```

<span class="exercise">**Exercise: demo 3 1**</span>
===

Find all "README"s, regardless of extension.

How many are there?


Finding by Name: Case Insensitive
=================================

- -name is case-sensitive.
- Use -iname instead to ignore case.

```bash
# find anything starting with "test"
# (case insensitive)
find . -iname 'test*'
```

<span class="exercise">**Exercise: demo 3 1**</span>
===
Find all "README"s, regardless of case or extension.

Finding by Type
===============

<!-- list_item_newlines: 1 -->
- By default, `find` searches for *both* files and directories.
    - Use `-type d` to search only for directories.
    - Use `-type f` to search only for files.

```bash
# find all directories starting with "test"
# (case-insensitive)
find . -iname 'test*' -type d

# find all files starting with "test"
# (case-insensitive)
find . -iname 'test*' -type f
```

<span class="exercise">**Exercise: demo 3 1**</span>
===

How many python test files are there? (Hint: they start with "test" and end with ".py")

The Need for Quotes
===================

At the root of the demo, try (without quotes):

```bash
find . -name test*
```

Then, with quotes:

```bash
find . -name 'test*'
```

The Need for Quotes
===================

<!-- list_item_newlines: 1 -->
- This is due to <span class="term">**shell expansion**</span>.
    - We will cover this in more detail later.
<!-- list_item_newlines: 2 -->
- In short: the * is being expanded *before* being passed to `find`.


Finding by Other Criteria
=========================

Can find files by **size**.

```bash
# find files larger than 1 megabyte
find . -size +1M

# find files smaller than 1 megabyte
find . -size -1M
```

Finding by Other Criteria
=========================

Can find files by **modification time**.

```bash
# find files modified in the last 7 days
find . -mtime -7

# find files modified more than 7 days ago
find . -mtime +7
```

Finding by Other Criteria
=========================

Can find files by:

- regular expressions
- what user owns them
- if they are executable or not
- etc.

Maximum Depth
=============

- By default, `find` searches recursively.
- Use `-maxdepth <N>` to limit how deep it searches.

```bash
# find all CSV files in the current directory,
# but not subdirectories
find . -maxdepth 1 -name '*.csv'

# find all CSV files in the current directory
# and its immediate subdirectories, but not deeper
find . -maxdepth 2 -name '*.csv'
```

<span class="exercise">**Exercise: demo 3 1**</span>
===

List the directories in the root of the demo.

Executing Commands on Found Items
=================================

- Great! we can find things.
- But what if we want to *do* something with those things?
- **Example**: delete all .DS_Store files in the project.


Executing Commands on Found Items
=================================


<!-- list_item_newlines: 1 -->
- Use `-exec` to run a command on each found file.
- Kind of a clunky syntax, but very powerful.
    - The `{}` is replaced with the file path.
    - Do *not* use quotes around the command!
    - The `\;` is required to terminate the command.

```bash
# find and delete all instances of .DS_Store
find . -name '.DS_Store' -exec rm {} \;
```

Tip
===

- Run the `find` command without `-exec` first to make sure it's finding the right files.
- For deleting in particular, rm -i is *interactive*. Will ask you to confirm before deleting each file.

```bash
# find and delete all instances of .DS_Store,
# asking for confirmation before deleting each one
find . -name '.DS_Store' -exec rm -i {} \;
```

Other Commands
==============

- You can run *any* command with `-exec`, not just `rm`.
<!-- list_item_newlines: 1 -->
- Other especially useful ones:
    - `cp` to copy files
    - `mv` to move/rename files
    - `touch <filename>` to create an empty file 

<span class="exercise">**Exercise: demo 3 1**</span>
===

Make a new directory named "backup", and copy *all* of the python files into
that directory.

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">grep</span>**


Finding by Content
==================

- *find* can only search by file name or metadata, not by file content.
- For that, we use the *grep* command.
- Returns all lines matching a pattern.

Two Main Use Cases
==================

We'll take a look at two main use cases for `grep`:

1. Searching a single file for a pattern.
2. Searching through many files for a pattern.

Searching a Single File
=======================

```bash
# search this file for the pattern
grep '<pattern>' <file>
```

Example:

```bash
# search README.md for the word "data"
grep 'data' README.md
```
<span class="bad">**Warning!**</span>
===

Note that the order is exactly opposite of `find`!

```bash
# in grep, pattern comes first
grep '<pattern>' <file>

# in find, pattern comes after the place to search
find <root-of-search> -name '<pattern>'
```

<span class="bad">**Warning!**</span>
===

- If you don't provide a file, `grep` waits for you to type input to search
  through.

```bash
grep 'foo'
```

- It will look like it's stuck.
- Press `<Ctrl-c>` to stop it.


<span class="exercise">**Exercise: demo 3 1**</span>
===

Find all lines in logs/training.log that contain "warning".

Case Insensitive Search
=======================

- By default, `grep` is case-sensitive.
- Use the `-i` flag to ignore case.

```bash
# find all lines in logs/training.log that contain
# "warning", ignoring case
grep -i 'warning' logs/training.log
```

Line Numbers
============

- Use the `-n` flag to include line numbers in the output.

```bash
# find all lines in logs/training.log that contain
# "WARNING", printing line numbers
grep -n 'WARNING' logs/training.log
```

Tip: Combining Flags
====================

Most commands that have multiple flags allow you to combine them.

```bash
# find all lines in logs/training.log that contain
# "warning", ignoring case and printing line numbers
grep -i -n 'warning' logs/training.log

# same, but more concise
grep -in 'warning' logs/training.log
```

Searching Through Many Files
============================

Use the -r flag to search through all files in a directory (recursively).

Example:

```bash
# search through all files in this directory
# (or any subdir) for the word "data"
grep -r 'data' .
```


<span class="exercise">**Exercise: demo 3 1**</span>
===

Search for the pattern "SECRET" throughout the whole demo directory.

Tip
===

The previous flags also work with -r:

```bash
# search through all files in this directory,
# ignoring case and printing line numbers
grep -rin 'data' .

# can add flags "after the fact", too
grep -r 'data' . -in
```

Puzzle
======

- We want to search for "TODO" throughout the project.
- But *only* in python files.
- How?

Idea
====

- Find the files with find.
- Call grep on each, using -exec.


```bash
# -H prints file name, -n prints line number
find . -name '*.py' -exec grep -nH 'TODO' {} \;
```

Even Simpler...
===============

- grep's --include flags let you specify a pattern to apply to filenames
- This is less flexible than find -exec.

```bash
# search for "TODO" in all python files
grep -rn --include='*.py' 'TODO' .
```

Regular Expressions
===================

- The pattern giving to `grep` can be a <span class="term">**regular expression**</span>.
- RegExes are powerful but cryptic.
- You'll learn (or learned) about them in DSC 80.

```bash
# find lines that start with "TODO"
grep '^TODO' <file>
```
