#!/usr/bin/python3
"""Provide a helper for checking whether an object inherits from a class."""


def inherits_from(obj, a_class):
    """Check whether obj inherits from a_class, excluding exact matches."""
    return isinstance(obj, a_class) and type(obj) is not a_class
