#!/usr/bin/python3
"""Define a base class with geometry validation helpers."""


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
