#!/usr/bin/python3
"""Define a student that supports dictionary serialization and reloading."""


class Student:
    """Represent a student whose attributes can be saved and restored."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student's public personal attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return attributes filtered by attrs when it is a list of strings."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Set instance attributes from the supplied dictionary."""
        self.__dict__.update(json)
