#!/usr/bin/python3
"""Define a square with a private size attribute."""


class Square:
    """Represent a square with a privately stored size."""

    def __init__(self, size):
        """Create a square and store its size without validation."""
        self.__size = size
