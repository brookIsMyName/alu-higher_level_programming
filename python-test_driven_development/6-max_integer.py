#!/usr/bin/python3
"""Find the largest integer in a list."""


def max_integer(list=[]):
    """Return the largest integer or None when the list is empty."""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
