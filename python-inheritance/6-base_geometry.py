#!/usr/bin/python3
"""Define a base class for geometry shapes."""


class BaseGeometry:
    """Represent the common interface for geometry classes."""

    def area(self):
        """Raise an exception because a generic shape has no defined area."""
        raise Exception("area() is not implemented")
