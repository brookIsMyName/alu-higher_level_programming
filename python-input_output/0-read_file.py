#!/usr/bin/python3
"""Provide a helper for printing UTF-8 text files."""


def read_file(filename=""):
    """Print the full contents of filename without adding a newline."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
