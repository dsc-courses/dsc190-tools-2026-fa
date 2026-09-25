# Syllabus

Welcome to DSC 190: Tools of the Trade.

This course introduces the essential tools of modern data science practice,
including version control with Git, shell scripting, Python environment
management, continuous integration and deployment, unit testing, deploying data
science models to production, and more. The class is designed from the start
around the meta-tool to rule all tools: *agentic AI*.

This course was first offered in Spring 2026, and it's still evolving. If you
have something you'd like to see covered, please let me know!

## Instructor

- Dr. Justin Eldridge ("Justin")
  [Website](https://eldridgejm.github.io)
  `jeldridge@ucsd.edu`

## Lectures and Discussion

- Lecture: Tuesdays and Thursdays, 5:00–6:20pm in Coalition Building B17.
  Attendance is optional, but it earns extra credit (see [Lecture
  Attendance](#lecture-attendance-extra-credit)).
- Discussion: Fridays, 4:00–4:50pm in Pepper Canyon Hall 121. This is where
  the weekly quizzes are held.

## Gradescope and Campuswire

We'll use Campuswire as the course messageboard and Gradescope for assignment
submission and grading. You should have received invitations to both. If not,
you can add yourself using the links and codes below:

- Gradescope
    - Link: https://www.gradescope.com/courses/1410894
    - Code: `68K8X5`
- Campuswire
    - Link: https://campuswire.com/p/G3D159E83
    - Code: `4507`

## Required Materials

To get the most out of this course, you will need access to an AI coding agent,
such as Anthropic's Claude Code or OpenAI's Codex -- in fact, some of the
assignments will *require* you to use one. Unfortunately, this means that you
*might* need to spend a little bit of money on an AI subscription. Luckily,
there are many good options available, and you can definitely get by with
spending less than $25 for the entire quarter.

We have put together a guide to help you decide on an AI agent subscription.
You can find it in the `resources/02-picking_an_ai/` directory of this
repository, as well as online at
<https://github.com/dsc-courses/dsc190-tools-2026-fa/tree/main/resources/02-picking_an_ai>.

## Grading

Your grade will be composed of three things:

- 8 Quizzes (40%)
- 8 Assignments (40%)
- Final Project (20%)

You can also earn up to 8% in extra credit by attending lecture.

### Weekly Quizzes

There will be 8 weekly quizzes. Each quiz will be held in-person at the
beginning of discussion section and will cover two lectures: Quiz 01 covers
Lectures 01 and 02, Quiz 02 covers Lectures 03 and 04, and so on. The first
quiz is on Friday, October 2.

Quizzes questions will be multiple choice and/or True/False. They will be
designed to be *very* quick, and each quiz will be timed to take 10 minutes.
The questions will not be deep conceptual questions -- rather, they will be
simple, "you know it or you don't" factual questions. An example of a quiz
question is:

```
What does the `-r` flag in `rm -r` do?

A) Remove read-only files without prompting
B) Remove directories and their contents recursively
C) Rename files instead of removing them
D) Reverse the most recent deletion
```

(The correct answer is B, in case you were wondering.)

**Preparing**. Each lecture directory has a file named `YSK.md` (short for "You
Should Know"). This file contains a list of questions about the material from
that lecture. The quiz will be a random selection of these questions,
so if you can do YSK questions, you'll do well on the quiz.

**Why?** The goal of this class is to get you *comfortable* with the tools of
the trade, so that using them becomes second nature. But you won't be
comfortable with a tool as long as every time you go to use it you have to stop
and look up how. Over time, you'll naturally build up a muscle memory -- and
that is where we want you to be eventually -- but that can take *years*. The
idea is that, by quizzing you regularly on the basics, we're encouraging you to
memorize their behavior, jumpstarting the process of building that muscle
memory.

**Cheat sheet**. Because the goal of the quiz is to encourage you to *memorize*
the basic behavior of the tools, you can't use a cheat sheet during the quiz.

#### Weekly Quiz Redemption

If you don't do well on a quiz, you'll have an opportunity to improve your
score the very next week by taking the *redemption* quiz. The redemption quiz
will also be held during discussion section, and it will cover the same
material as the original quiz, but it will be a different set of questions (also
drawn from the YSK file). Details about the redemption quiz will be provided before
the first redemption quiz.

*Note*: you do *not* need to have taken the original quiz in order to take the
redemption. So, if you're really dreading the idea of coming to discussion *every
week*, you can just come every other week and take the quiz for that week
and the week before. Of course, by doing so, you're only getting one shot at
each quiz, so it's a bit riskier.

#### The "Too Cool for School" Option

If you don't want to take weekly quizzes, you can instead opt to take a single,
comprehensive, oral exam with me during Week 10 of the quarter. You will be
graded on a coarse 5-point scale reflecting your overall understanding of the
material. The content of the exam will be similar to the weekly quizzes, but it
won't be multiple choice. For example, I might simply ask: "What does the `-r`
flag in `rm -r` do?" and you would have to answer in your own words.

If you want to do this option, you must let me know via email by the end of
Week 2. You can't change your mind after that -- once you opt for the oral
exam, it's set in stone!

### Weekly Assignments

There will also be 8 weekly assignments. The format and structure of the
assignments will naturally vary from week to week as we learn different tools,
but they will always be due on Tuesday at 11:59 pm. You will turn them in on
Gradescope (unless otherwise specified in the assignment instructions).

The purpose of the assignments is twofold. First, they will often introduce and
walk you through the use of new tools (or aspects of tools) that we can only
briefly cover in lecture. Second, they will give you the opportunity to
practice the tools in a more realistic setting, hopefully demonstrating why
they are useful and how they fit into a data science workflow.

Assignments will be autograded according to a rubric that will be provided
along with the assignment itself. This will allow you to verify for yourself
that your submission meets all of the requirements for full credit before you
turn it in.

**Slip days.** You will have 4 slip days to use on any assignment (or the final
project). A slip day allows you to turn in an assignment up to 24 hours late
without penalty. Slip days don't "stack": you can only use one per assignment.

### Final Project

There will be a final project due at the end of the quarter, during finals
week. Details about the final project will be released towards the end of the
quarter.

### Lecture Attendance (Extra Credit)

Lecture attendance is optional, but each lecture you attend earns you half a
percentage point of extra credit on your final grade, up to a maximum of 8%
(that is, 16 lectures). We'll start taking attendance in Lecture 02. This
applies to everyone, including those who choose the "Too Cool for School"
option.

## Artificial Intelligence and Collaboration Policy

You are *encouraged* to use AI tools on any and all assignments in this class
(including the final project). In fact, some of the assignments will *require*
you to use them. We will sometimes make recommendations about when you
*shouldn't* use AI (for instance, you should probably be comfortable moving
around the file system without using an AI agent), but we can't (and won't)
enforce these recommendations.

You can also discuss the assignments with your fellow students, but you have to
turn in your own work. You can't copy and paste from each other, for example.
The same goes for the final project -- you can talk to your classmates about
it, but you have to turn in separate projects (it is not a group project).

Of course, you cannot use AI or collaborate on the quizzes.
