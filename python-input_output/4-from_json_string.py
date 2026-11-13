#!/usr/bin/python3
"""Provide a helper for decoding JSON strings into Python objects."""
import json


def from_json_string(my_str):
    """Return the Python object represented by the JSON string my_str."""
    return json.loads(my_str)
