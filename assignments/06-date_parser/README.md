# Assignment 06: Natural-Language Date Parser

**Due**: Tuesday, November 10 at 11:59 PM on Gradescope

In this week's lectures, we saw tools such as pytest, mypy, and ruff that help
us write good code. We also saw a demonstration of coding agents, and how these
tools (pytest in particular) play a role in what we called the "middle path"
workflow for developing software with AI, where we (the human) write a precise
specification in the form of a test suite, and the AI fills in the
implementation.

In this assignment, you'll use this workflow to build a small Python library
called `nldate` that turns natural-language date strings — things like `"5 days
before December 1st, 2025"` and `"next Tuesday"` — into concrete dates.

This is a place where the "middle path" workflow shines. The tests are easy and
quick to write, since it is straightforward to specify the expected output for
a given input. The implementation, on the other hand, is tricky to write by
hand. There are a lot of corner cases and branches to get right, and it's easy
to make a small mistake. In the "middle path", we let the AI agent handle the
implementation, and the test cases will serve as guardrails to ensure it gets
the right answer.

## The Scenario

You've just started working at a company whose main product is a calendar app.
The CEO has caught the AI bug, and they want to see AI features added to the
app. "Users should be able to write a date in English, like 'two weeks from
tomorrow' and have the AI figure out what date they mean," they tell your
project manager. Your project manager, though, is smart: they realize that "AI"
(in the form of an LLM or similar) is overkill for a task like this (and an
expensive overkill at that). Rather, some basic pattern matching is all you
need.

Your PM sends you an email at 4:30 pm on Friday afternoon laying out the task.

> Hey UCSD DSC graduate,
>
> We need to get some natural date parsing into the calendar app ASAP so we
> can stay front-footed on the AI trend.
>
> Could you write up a Python package that takes in a natural language date,
> like "5 days before December 1st, 2025", "1 year and 2 months after
> yesterday", or "next Tuesday", and returns a `datetime.date` object?
>
> Please have it in my queue for review by the open of business on Monday.
>
> Thanks! Have a good weekend!
>
> Sincerely,
> Boss

Your boss then stops by your desk before they leave the office and fills in some
details. They are expecting you to write a Python package named `nldate` that
has a `parse()` function with the following signature:

```python
from datetime import date

def parse(s: str, today: date | None = None) -> date:
    ...
```

Given a natural language date, like "5 days before December 1st, 2025" or "next
Tuesday", the `parse()` function should return a `datetime.date` object
representing the date that the input string refers to. The `today` parameter is
used as a reference point for relative date expressions (like "next Tuesday" or
"in 3 days"). If `today` is not provided, it should default to the current
date.

You ask your boss: "what, exactly, can the input look like? Can you give me a
list of all the different formats I need to support?" They say: "Sorry, I don't
have time to write up a spec right now. Can you just make it work for the most
common kinds of input you can think of? I'm sure you'll figure it out! If you
send me a working implementation over the weekend, I'll test it on a bunch of
inputs and let you know what to add support for."

## Requirements

- You should implement your code in a public GitHub repository.
- Your project should be a Python package named `nldate`, managed with `uv`
  and created with `uv init --package nldate` (so that your code lives under
  `src/nldate/`). Commit the `uv.lock` file.
- `pytest`, `mypy`, and `ruff` should be dev dependencies of your project.
- Your project should contain a `tests/` directory containing a pytest test
  suite with at least 10 tests. All tests must pass with `uv run pytest`.
- `uv run mypy src/`, `uv run ruff check`, and `uv run ruff format --check`
  should all pass with no errors on your codebase.
- If `parse()` is given a string that isn't a date it recognizes (including
  the empty string), it should raise a `ValueError`.

## The Autograder

Submit to the autograder a single file named `repo_url.txt` containing the URL
of your GitHub repository. Make sure that your repo is public, as otherwise the
autograder won't be able to access it.

The autograder for this assignment will clone your repository and check that
the above requirements are met. It will also test your `parse()` function on a
variety of inputs. However, as soon as one of the test cases fails, the
autograder will stop and report that failure without proceeding, similar to
what your boss would do in real life when they are testing your implementation.
Because of this, you should start by writing a date parser that is very general
and accepts a wide variety of date formats -- not just those that your boss
specified in their original email.

All of the autograder's tests are public, so if you pass all of them, you will
get full credit on this assignment.
