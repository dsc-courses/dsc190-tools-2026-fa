---
theme:
  path: ../../.presenterm/theme.yaml
options:
  list_item_newlines: 2
---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Lecture 02 — The Shell</span>**

The Shell
=========

- Welcome back.
- Open a terminal on your computer (Windows: the Ubuntu app) and clone the course repo:
    - `git clone https://github.com/dsc-courses/dsc190-tools-2026-fa.git`
    - You will only need to do this once.
    - Mac: if asked to install developer tools, say yes (it takes a few minutes).
- Then, start the Linux environment:
    - `cd dsc190-tools-2026-fa`
    - `bash start-linux.sh`
- When inside the container, update its copy of the repo:
    - `cd dsc190-tools-2026-fa`
    - `git pull`

Demo 01
=======

We left off with Demo 01...

Tips
====

Use the keyboard shortcuts!

<!-- list_item_newlines: 1 -->
- Up/down arrows: cycle through command history
- Ctrl-a / Ctrl-e: move to beginning/end of line
- Ctrl-u: delete from cursor to beginning of line
- Ctrl-w: delete previous word
- Alt-left/right: move cursor one word left/right

Example: `mdkir foo bar baz`

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Agents</span>**

---

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

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Quiz 01</span>**

Quiz 01
=======

- This Friday, in discussion section.
- 10 questions, 10 minutes.
    - We'll actually do 20 minutes this time, since it's a new format.
- Prepare using the `YSK.md` files.
- Afterwards, I'll talk about some topic for fun.

Quiz Me
=======

Try opening *opencode* in the DSC 190 course repo and asking "Quiz Me".
