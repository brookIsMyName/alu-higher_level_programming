#!/usr/bin/python3
"""Provide a helper for inspecting an object's available names."""


def lookup(obj):
    """Return the names of attributes and methods available on an object."""
    return dir(obj)
