"""Setup script for Assignment 02.

Creates sample data for the assignment. Students can delete the data/ directory
and re-run this script to regenerate.
"""

import os
import shutil
import random

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
TEMPS_DIR = os.path.join(DATA_DIR, "temperatures")

random.seed(42)

STATIONS = [
    "san_diego", "los_angeles", "san_francisco", "sacramento",
    "fresno", "oakland", "santa_barbara",
]


def setup_temperatures():
    """Create temperature CSV files with inconsistent date zero-padding."""
    os.makedirs(TEMPS_DIR)

    dates = []
    for month in [1, 2, 3, 6, 10, 11, 12]:
        for day in [1, 3, 7, 9, 14, 21, 28]:
            if month == 2 and day > 28:
                continue
            dates.append((2025, month, day))

    selected = random.sample(dates, 30)
    selected.sort()

    for year, month, day in selected:
        station = random.choice(STATIONS)

        pad_month = random.choice([True, False])
        pad_day = random.choice([True, False])
        m_str = f"{month:02d}" if pad_month else str(month)
        d_str = f"{day:02d}" if pad_day else str(day)

        # ~30% of files use MM-DD-YYYY instead of YYYY-MM-DD
        if random.random() < 0.3:
            date_str = f"{m_str}-{d_str}-{year}"
        else:
            date_str = f"{year}-{m_str}-{d_str}"

        fname = f"{station}_temperature_{date_str}.csv"

        filepath = os.path.join(TEMPS_DIR, fname)
        with open(filepath, "w") as f:
            f.write("hour,temperature_f\n")
            for hour in range(0, 24, 3):
                temp = random.randint(45, 95)
                f.write(f"{hour},{temp}\n")

    print(f"Created {len(selected)} temperature files in {TEMPS_DIR}")


def main():
    if os.path.exists(DATA_DIR):
        shutil.rmtree(DATA_DIR)

    setup_temperatures()


if __name__ == "__main__":
    main()
