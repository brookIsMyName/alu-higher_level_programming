#!/usr/bin/python3
"""Define a square with a readable description and area."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square whose sides have equal length."""

    def __init__(self, size):
        """Initialize the square after validating its side length."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the square dimensions in the required display format."""
        return "[Square] {}/{}".format(self.__size, self.__size)
