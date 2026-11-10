#!/usr/bin/python3
"""Define a square with a position and print support."""


class Square:
    """Represent a positioned square with validated attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Create a square and set its validated size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the square's printing position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Validate and update the square's printing position."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(item, int) and item >= 0
                        for item in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of this square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with its configured indentation."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
