#!/usr/bin/python3
"""Provide a helper for checking an object's exact class."""


def is_same_class(obj, a_class):
    """Return whether obj's exact class is a_class."""
    return type(obj) is a_class
