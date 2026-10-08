"""Part 5 worked example: summarize completion rates per user from a web API.

Needs the requests package:  pip install requests
Run:  python summarize_todos.py     (writes output/summary.json next to this file)
"""
import json
from pathlib import Path

import requests

URL = "https://jsonplaceholder.typicode.com/todos"
OUTPUT = Path(__file__).parent / "output" / "summary.json"


def fetch_todos(url):
    """Download the to-do records and return them as Python objects."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def completion_by_user(todos):
    """Return a dict mapping each user id to a (completed, total) tuple."""
    counts = {}
    for todo in todos:
        user = todo["userId"]
        done, total = counts.get(user, (0, 0))
        # int(True) is 1 and int(False) is 0, so this adds 1 only if completed.
        counts[user] = (done + int(todo["completed"]), total + 1)
    return counts


def completion_rates(counts):
    """Convert (completed, total) pairs into percentages."""
    return {user: round(100 * done / total, 1)
            for user, (done, total) in counts.items()}


def main():
    try:
        todos = fetch_todos(URL)
    except requests.RequestException as error:
        print(f"Download failed: {error}")
        raise SystemExit(1)

    counts = completion_by_user(todos)
    rates = completion_rates(counts)

    # max with key=rates.get returns the KEY whose VALUE is largest.
    # If several users tie for the top rate, max returns whichever comes first.
    best = max(rates, key=rates.get)
    summary = {
        "records": len(todos),
        "users": len(rates),
        "rates": rates,
        "most_complete_user": best,
    }

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"Read {len(todos)} records for {len(rates)} users.")
    print(f"User {best} has the highest completion rate at {rates[best]}%.")
    print(f"Summary written to {OUTPUT}")


# This guard stops main() running when the file is imported.
if __name__ == "__main__":
    main()
