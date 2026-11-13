#!/usr/bin/python3
"""Provide a helper for loading Python objects from JSON files."""
import json


def load_from_json_file(filename):
    """Return the Python object represented by the JSON in filename."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
