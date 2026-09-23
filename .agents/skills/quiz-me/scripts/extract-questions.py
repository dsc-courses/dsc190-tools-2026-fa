#!/usr/bin/env python3
"""Extract questions and answers from YSK.md files.

Usage:
    extract-questions.py <ysk-file> [<ysk-file> ...]

Outputs a JSON array of objects with keys: topic, question, answer, source.
"""

import json
import re
import sys


def extract(path: str) -> list[dict]:
    questions = []
    topic = ""
    pending_question = None

    with open(path) as f:
        for line in f:
            # Topic heading
            if m := re.match(r"^#\s+(.+)", line):
                topic = m.group(1).strip()
                continue

            # Question bullet
            if m := re.match(r"^- (.+\?)\s*$", line):
                # Save any previous question that had no answer
                if pending_question:
                    questions.append(pending_question)
                pending_question = {
                    "topic": topic,
                    "question": m.group(1).strip(),
                    "answer": "",
                    "source": path,
                }
                continue

            # Answer bullet (indented under a question)
            if pending_question and (m := re.match(r"^\s+- \*\*Answer\*\*:\s*(.+)", line)):
                pending_question["answer"] = m.group(1).strip()
                questions.append(pending_question)
                pending_question = None
                continue

    # Catch trailing question with no answer
    if pending_question:
        questions.append(pending_question)

    return questions


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print((__doc__ or "").strip(), file=sys.stderr)
        sys.exit(1)

    all_questions = []
    for path in sys.argv[1:]:
        all_questions.extend(extract(path))

    json.dump(all_questions, sys.stdout, indent=2)
    print()
