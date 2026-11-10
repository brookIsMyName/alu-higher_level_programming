#!/usr/bin/python3
"""Define a square with a validated, accessible size."""


class Square:
    """Represent a square with validated size and area calculation."""

    def __init__(self, size=0):
        """Create a square and set its validated size."""
        self.size = size

    @property
    def size(self):
        """Return the square's size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate and update the square's size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of this square."""
        return self.__size * self.__size
