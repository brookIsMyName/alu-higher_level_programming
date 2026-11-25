#!/usr/bin/python3
"""Define a rectangle with validated dimensions and display offsets."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle that can render and serialize its geometry."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle's identifier, dimensions, and offsets."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def _validate_integer(name, value, minimum):
        """Require an integer at or above the dimension or offset minimum."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < minimum:
            limit = "> 0" if minimum == 1 else ">= 0"
            raise ValueError("{} must be {}".format(name, limit))

    @property
    def width(self):
        """Return the positive horizontal dimension."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width to a positive integer."""
        self._validate_integer("width", value, 1)
        self.__width = value

    @property
    def height(self):
        """Return the positive vertical dimension."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height to a positive integer."""
        self._validate_integer("height", value, 1)
        self.__height = value

    @property
    def x(self):
        """Return the number of spaces that precede each display row."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal offset to a nonnegative integer."""
        self._validate_integer("x", value, 0)
        self.__x = value

    @property
    def y(self):
        """Return the number of empty lines above the displayed shape."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical offset to a nonnegative integer."""
        self._validate_integer("y", value, 0)
        self.__y = value

    def area(self):
        """Return the product of the current width and height."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using hash characters and both offsets."""
        print("\n" * self.y, end="")
        row = " " * self.x + "#" * self.width
        for _ in range(self.height):
            print(row)

    def __str__(self):
        """Return the rectangle's identifier, offsets, and dimensions."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def _update_attributes(self, fields, args, kwargs):
        """Apply recognized fields and give positional arguments priority."""
        updates = zip(fields, args) if args else kwargs.items()
        for name, value in updates:
            if name == "id" and value is None:
                Base.__init__(self)
            elif name in fields:
                setattr(self, name, value)

    def update(self, *args, **kwargs):
        """Set id, width, height, x, and y from the supplied arguments."""
        self._update_attributes(("id", "width", "height", "x", "y"),
                                args, kwargs)

    def to_dictionary(self):
        """Return the identifier and geometry as a new dictionary."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
