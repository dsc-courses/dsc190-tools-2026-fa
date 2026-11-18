"""
Sample water temperature at the Scripps Pier in La Jolla over the course
of about an hour, and write the readings to readings.csv.

Uses only the Python standard library. Queries NOAA's tides & currents
API (station 9410230, Scripps Pier, La Jolla) once every five minutes,
for a total of twelve readings.
"""

import csv
import json
import sys
import time
import urllib.request

STATION = "9410230"  # Scripps Pier, La Jolla
URL = (
    "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
    f"?station={STATION}&product=water_temperature"
    "&date=latest&units=metric&time_zone=gmt&format=json"
)
N_SAMPLES = 12
INTERVAL_SECONDS = 5 * 60
OUTPUT_FILE = "readings.csv"

# If a request to NOAA fails (a timeout, a server error, or a response
# without any data), wait a bit and try again rather than crashing.
MAX_ATTEMPTS = 5
RETRY_DELAY_SECONDS = 30


def fetch_latest_reading():
    with urllib.request.urlopen(URL, timeout=30) as response:
        payload = json.loads(response.read())
    point = payload["data"][0]
    return point["t"], point["v"]


def fetch_latest_reading_with_retries():
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            return fetch_latest_reading()
        except (OSError, ValueError, KeyError, IndexError) as exc:
            # OSError covers network errors and timeouts; ValueError covers
            # bad JSON; KeyError and IndexError cover a response with no data.
            if attempt == MAX_ATTEMPTS:
                raise
            print(
                f"request failed ({exc!r}); retrying in "
                f"{RETRY_DELAY_SECONDS} seconds "
                f"(attempt {attempt}/{MAX_ATTEMPTS})",
                flush=True,
            )
            time.sleep(RETRY_DELAY_SECONDS)


def main():
    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "water_temp_c"])
        for i in range(N_SAMPLES):
            timestamp, value = fetch_latest_reading_with_retries()
            writer.writerow([timestamp, value])
            f.flush()
            print(
                f"sample {i + 1}/{N_SAMPLES}: {timestamp} -> {value} C",
                flush=True,
            )
            if i < N_SAMPLES - 1:
                time.sleep(INTERVAL_SECONDS)
    print(f"wrote {N_SAMPLES} readings to {OUTPUT_FILE}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
