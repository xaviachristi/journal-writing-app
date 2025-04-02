"""Functions to manage entries"""

from json import load
from uuid import uuid4  # generates ids almost guaranteed to be unique
from datetime import datetime


def load_all_entries(filename: str = "data.json") -> list[dict]:
    """Returns entries from a data file."""

    with open(filename, "r", encoding="utf-8") as file:
        entries = load(file)

    return entries


def is_valid_entry(entry: dict) -> bool:
    """Returns if an entry is valid."""

    for k in ["body", "author"]:
        if k not in entry or not entry[k]:
            return False
    return True


def save_new_entry(entry: dict, filename: str = "data.json") -> dict:
    """Saves an entry to a data file."""

    entries = load_all_entries(filename)

    entry["id"] = uuid4()
    if "title" not in entry:
        entry["title"] = None
    entry["created_at"] = datetime.now().isoformat()
    entries.append(entry)

    with open(filename, "w", encoding="utf-8") as file:
        dump(entries, file, indent=4)

    return entry
