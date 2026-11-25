#!/usr/bin/python3
"""Print a person's name in a short introduction."""


def say_my_name(first_name, last_name=""):
    """Validate both names as strings and print the introduction."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
