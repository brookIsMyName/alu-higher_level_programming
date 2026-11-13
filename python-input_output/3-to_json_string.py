#!/usr/bin/python3
"""Provide a helper for serializing objects as JSON strings."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of my_obj."""
    return json.dumps(my_obj)
