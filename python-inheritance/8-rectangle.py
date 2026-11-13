#!/usr/bin/python3
"""Define a rectangle with validated dimensions."""

class BaseGeometry:
    """Represent the common interface and validation for geometry classes."""

    def area(self):
        """Raise an exception because a generic shape has no defined area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer, using name in errors."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represent a rectangle with private width and height dimensions."""

    def __init__(self, width, height):
        """Initialize the rectangle after validating both dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
