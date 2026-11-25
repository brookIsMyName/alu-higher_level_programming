#!/usr/bin/python3
"""Print a square using hash characters."""


def print_square(size):
    """Print a square with the specified nonnegative integer side length."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    row = "#" * size
    for _ in range(size):
        print(row)
