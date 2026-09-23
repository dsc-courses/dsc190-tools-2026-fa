---
name: quiz-me
description: Quiz a student on lecture material using YSK (You Should Know) questions. Use when user wants to be quizzed, test their knowledge, review for an exam, or mentions "quiz me".
---

# Quiz Me

Quiz a student on lecture material by sampling from YSK.md files.

## Background

Each lecture directory (`lectures/01-intro/`, `lectures/02-shell/`, etc.) may contain a `YSK.md` ("You Should Know") file. These are collections of short-answer recall questions organized by topic, covering the key concepts from that lecture. Each question has an expected answer inline.

## Setup

1. Determine scope: does the student want questions from a specific lecture, a certain week's lectures, a specific topic, or all lectures?
   - Specific lecture: use that lecture's `YSK.md` (e.g., `lectures/02-shell/YSK.md`).
   - Specific topic (e.g., "the cd command"): extract from all YSK files, then filter the JSON to questions whose `topic` matches.
   - All lectures: glob for `lectures/*/YSK.md` and pass all matches.
2. Extract and shuffle questions using the helper scripts:
   ```
   python3 .agents/skills/quiz-me/scripts/extract-questions.py <ysk-files...> \
     | python3 .agents/skills/quiz-me/scripts/sample-questions.py <N>
   ```

## Asking Questions

Present questions one at a time:

1. Show the question number and topic (e.g., "**Question 2 of 5** — The `cd` command").
2. Ask the question and wait for the student's answer.
3. After they answer:
   - If correct (or close enough), confirm and move to the next question.
   - If wrong, give a brief hint and let them try once more before revealing the answer.
4. Keep a running score.

## Wrapping Up

After the last question, show the student's final score (e.g., "You got 4 out of 5") and list any questions they missed with the correct answers.
