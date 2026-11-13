#!/usr/bin/python3
"""Provide a helper for checking class membership and inheritance."""


def is_kind_of_class(obj, a_class):
    """Return whether obj is an instance of a_class or one of its subclasses."""
    return isinstance(obj, a_class)
