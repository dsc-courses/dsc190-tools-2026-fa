#!/usr/bin/env python3
"""Randomly sample questions from extracted YSK JSON.

Usage:
    extract-questions.py <files...> | sample-questions.py [N]
    sample-questions.py [N] < questions.json

N defaults to 5. Pass 0 for all questions (shuffled).
"""

import json
import random
import sys


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5

    questions = json.load(sys.stdin)

    if n == 0 or n >= len(questions):
        random.shuffle(questions)
        sampled = questions
    else:
        sampled = random.sample(questions, n)

    json.dump(sampled, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
