# Assignment 01: The Haunted Server
**Due**: Tuesday, October 6 at 11:59 PM on Gradescope


During renovations of the HDSI building -- which had previously housed the
literature department since the early days of the university -- workers
discovered a dusty old PDP-11 minicomputer in the basement. As they moved it, a
small sign fell off and went unnoticed. The sign read: **"DO NOT TURN ON!"**

Naturally, someone turned it on.

The machine was running Unix Version 4 (released in 1973), and its file system
was still intact -- home directories of researchers and faculty who had left
decades ago, old project files, system logs, and half-finished manuscripts. But
something was off. Scattered across the file system were strange messages --
fragments that didn't belong to any user, references to something called
**PHANTOM**, and codewords hidden in places no one should have been writing to.

No one knows who left them there. Campus IT has made a copy of the file system
and they're asking for your help investigating it.

## Your Mission

Navigate the old file system, follow PHANTOM's trail, and recover the **8
codewords** hidden along the way. You will need to use `ls`, `cd`, `less`,
`find`, and `grep` to track them down.

## Getting Started

Open your docker container, `cd` into the course repo, and run `git pull`. Then
navigate to this assignment directory and run:

```
bash start.sh <your email>
```

Use your email address **exactly as it appears on Gradescope**, including the
`@ucsd.edu` part (e.g., `bash start.sh jdoe@ucsd.edu`). Each student gets a
different trail based on their email, and the autograder uses your Gradescope
email to check your answers. If you use a different address (like an alias),
you'll be following someone else's trail and the autograder won't accept your
codewords.

This will download the data into `filesystem/` and give you instructions on
where to find the first clue.

Each clue you find will contain a codeword and a hint telling you how to find
the next one. Keep track of these codewords -- it's what you'll turn in.

**A note on paths:** The clues reference paths like `/home/...` or `/var/...`.
These are paths *inside* the old file system. On your machine, they live under
the `filesystem/` directory. So `/home/thornton` means
`filesystem/home/thornton`.

**A note on commands:** All of the clues are solvable with the commands we learned
(`ls`, `cd`, `less`, `find`, `grep`), but some of them might require options or
features we *didn't* cover in lecture. That's intentional: you should use
`--help`, `man`, `tldr` -- or ask an AI -- to figure out how to use the
commands in new ways. Reading the manual is a key part of working with any new
tool, after all.

## Submission

Once you have collected all 8 codewords, create a file called `answers.txt`
with one codeword per line (in the order you found them) and submit it to
Gradescope. Your submission must contain all 8 codewords -- partial submissions
will not be graded. The autograder is entirely public -- if you pass all of
the tests you have the right codewords in the right order and you'll get full
credit.
