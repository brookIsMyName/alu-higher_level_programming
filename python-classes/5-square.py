#!/usr/bin/python3
"""Define a square that can calculate and print its shape."""


class Square:
    """Represent a square with validated size and print support."""

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

    def my_print(self):
        """Print the square using hash characters."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
