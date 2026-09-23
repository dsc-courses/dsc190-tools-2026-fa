---
name: walkthrough
description: Walk a student through a lecture demo interactively, step by step. Use when user wants to practice a demo, do a walkthrough, or work through a lecture exercise.
---

# Demo Walkthrough

Walk a student through a lecture demo one step at a time.

## Setup

1. Identify the demo to walk through. Demos live in `lectures/*/demos/*/`. If you're started from within a demo directory, you're already in the right place.
2. Read the demo's `README.md` to get the full list of steps.

## Walking Through Steps

Present one step at a time. For each step:

1. **Explain** the concept or command being introduced — keep it brief.
2. **If the step has a Task** that requires a shell command:
   - Ask the student to provide the command they would run.
   - If their command isn't quite right, give a short hint and let them try again. Don't just give them the answer immediately.
   - Once they have it right (or close enough), run the command and show them the output.
3. **If the step has a Question**:
   - Ask the student the question and wait for their answer.
   - Provide feedback: confirm if correct, or gently guide them toward the right answer with a follow-up hint.
4. **If the step is purely informational** (no task or question):
   - Explain the concept, demonstrate the commands mentioned, and move on.
