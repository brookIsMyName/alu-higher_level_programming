#!/usr/bin/python3
"""Define a list subclass with a sorted display method."""


class MyList(list):
    """Represent a list that can display its values in sorted order."""

    def print_sorted(self):
        """Print the list values in ascending order without changing the list."""
        print(sorted(self))
