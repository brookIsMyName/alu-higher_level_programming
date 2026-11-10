#!/usr/bin/python3
"""Define a square with a validated size."""


class Square:
    """Represent a square whose size is a non-negative integer."""

    def __init__(self, size=0):
        """Create a square after validating its size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
