#!/usr/bin/python3
"""Provide a helper for writing UTF-8 text files."""


def write_file(filename="", text=""):
    """Overwrite filename with text and return the characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
