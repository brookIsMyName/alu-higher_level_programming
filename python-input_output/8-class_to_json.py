#!/usr/bin/python3
"""Provide a dictionary representation of an object's attributes."""


def class_to_json(obj):
    """Return the instance attribute dictionary of obj for serialization."""
    return obj.__dict__
