#!/usr/bin/python3
"""Add two integers, converting floating-point arguments first."""


def add_integer(a, b=98):
    """Convert numeric arguments to integers and return their sum."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
