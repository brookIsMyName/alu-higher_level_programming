#!/usr/bin/python3
"""Define a rectangle with dimensions, area, and a readable description."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with validated private dimensions."""

    def __init__(self, width, height):
        """Initialize the rectangle after validating both dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle dimensions in the required display format."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
