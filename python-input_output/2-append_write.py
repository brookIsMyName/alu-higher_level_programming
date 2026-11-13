#!/usr/bin/python3
"""Provide a helper for appending text to UTF-8 files."""


def append_write(filename="", text=""):
    """Append text to filename and return the number of characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
