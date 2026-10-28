---
theme:
  path: ../../../.presenterm/theme.yaml
options:
  list_item_newlines: 2
---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../../COMMON/logo.png)

**<span class="term">Extra: Modern Shell</span>**

Modern Shell
============

- The tools we've been learning (bash, find, grep, *et al.*) are 30, 40, 50 years old.
<!-- list_item_newlines: 1 -->
- Today: we'll see some more *modern* replacements.
    - Nicer to use, more powerful, faster.

So why learn the old tools?
===========================

Two reasons:

<!-- list_item_newlines: 1 -->
1. They are everywhere.
    - bash, find, grep, *et al.* are on *every* Unix/Linux system.
    - The modern tools we'll see today are usually *not*.
<!-- list_item_newlines: 2 -->
2. AI agents love to use the old tools.

Today's Tools
=============

- bash -> fish
- ls -> lsd
- less -> bat
- find -> fd
- grep -> rg (ripgrep)
- cd -> zoxide
- ? -> fzf

Installation
============

- Unlike the old tools, these modern ones are typically not installed by default.
- I have already installed them for you in the linux container.
- To install them on your machine:
    - MacOS: use homebrew
    - Windows (via WSL): use apt


bash
====

- There are many different shells.
- The shell we have been using is called *`bash`*
    - "Bourne Again SHell"
- It has been the default since 1989.

1989
====

![image:w:60%](./fig/1989.png)

fish
====

- *fish* ("Friendly Interactive SHell") is a more modern shell.
- Type "`fish`" to start it.
- Features:
    - Better auto-completion
    - Color!
    - More!
- Only *somewhat* bash-compatible.

lsd
===

- lsd ("LSDeluxe") is a modern replacement for `ls`.
- Type "`lsd`" to use it.
- Features:
    - Color!
    - Icons!

bat
===

- `bat` is a modern replacement for `less` (and `cat`).
- Type "`bat <filename>`" to use it.
- Features:
    - Color!
    - Line numbers!

fd
==

- `fd` is a modern replacement for `find`.
- Type "`fd <pattern>`" to use it.
- Features:
    - Faster!
    - Simpler syntax!

```bash
fd "pattern"
# vs.
find . -name "*pattern*"
```

rg
==

- `rg` ("ripgrep") is a modern replacement for `grep`.
- Type "`rg <pattern>`" to use it.
- Features:
    - Faster!
    - Simpler syntax!

```bash
rg "pattern"
# vs.
grep -r "pattern" .
```

zoxide
======

- `zoxide` is a modern replacement for `cd`.
- By default, every time you `cd` into a directory, zoxide remembers it.
- Now, you can "jump" to that directory by typing `z <pattern>`, where `<pattern>` is a substring of the directory name.

fzf
===

- The modern shell can be much more *interactive*.
- `fzf` is a command-line "fuzzy finder".
- Reads "choices" from standard input, and lets you interactively select one.

Demo: zoxide + fzf
==================

- By default, `zi` runs fzf populated with directories you can jump to.
