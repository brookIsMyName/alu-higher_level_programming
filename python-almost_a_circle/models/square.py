#!/usr/bin/python3
"""Define a square using the dimensions and offsets of a rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent an equal-sided rectangle with a size property."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize both dimensions from the same side length."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the square's identifier, offsets, and size."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )

    @property
    def size(self):
        """Return the current side length."""
        return self.width

    @size.setter
    def size(self, value):
        """Validate and assign the new width and height in that order."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Set id, size, x, and y from the supplied arguments."""
        self._update_attributes(("id", "size", "x", "y"), args, kwargs)

    def to_dictionary(self):
        """Return the identifier, size, and offsets as a new dictionary."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
