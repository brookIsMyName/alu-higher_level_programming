#!/usr/bin/python3
"""Define a square that can calculate its area."""


class Square:
    """Represent a square and calculate its area."""

    def __init__(self, size=0):
        """Create a square after validating its size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of this square."""
        return self.__size * self.__size

