#!/usr/bin/python3
"""Test rectangle construction, validation, rendering, and updates."""
from contextlib import redirect_stdout
from io import StringIO
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Check Rectangle operations against their documented contracts."""

    def test_constructor_and_properties(self):
        """Initialize dimensions, offsets, and ID and allow valid changes."""
        rect = Rectangle(4, 6, id=12)
        self.assertIsInstance(rect, Base)
        self.assertEqual((rect.id, rect.width, rect.height, rect.x, rect.y),
                         (12, 4, 6, 0, 0))
        rect.width, rect.height, rect.x, rect.y = 2, 8, 3, 4
        self.assertEqual((rect.width, rect.height, rect.x, rect.y),
                         (2, 8, 3, 4))

    def test_missing_arguments(self):
        """Require both dimensions when constructing a rectangle."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_invalid_types(self):
        """Reject invalid attribute types in constructors and setters."""
        rect = Rectangle(3, 4, id=1)
        for name in ("width", "height", "x", "y"):
            for value in (True, False, 2.0, "2", None, [], {}):
                with self.subTest(name=name, value=value):
                    message = "^{} must be an integer$".format(name)
                    fields = {"width": 3, "height": 4, name: value}
                    with self.assertRaisesRegex(TypeError, message):
                        Rectangle(id=1, **fields)
                    with self.assertRaisesRegex(TypeError, message):
                        setattr(rect, name, value)

    def test_invalid_ranges(self):
        """Enforce positive dimensions and nonnegative offsets."""
        rect = Rectangle(3, 4, id=1)
        for name in ("width", "height", "x", "y"):
            dimension = name in ("width", "height")
            values = (-1, 0) if dimension else (-1,)
            limit = "> 0" if dimension else ">= 0"
            message = "^{} must be {}$".format(name, limit)
            for value in values:
                with self.subTest(name=name, value=value):
                    fields = {"width": 3, "height": 4, name: value}
                    with self.assertRaisesRegex(ValueError, message):
                        Rectangle(id=1, **fields)
                    with self.assertRaisesRegex(ValueError, message):
                        setattr(rect, name, value)
        self.assertEqual(rect.to_dictionary(),
                         {"id": 1, "width": 3, "height": 4, "x": 0, "y": 0})

    def test_area_and_string(self):
        """Compute area and represent a rectangle with all its fields."""
        rect = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rect.area(), 24)
        self.assertEqual(str(rect), "[Rectangle] (12) 2/1 - 4/6")
        rect.width = 5
        self.assertEqual(rect.area(), 30)

    def test_display(self):
        """Write one line per row and apply both display offsets."""
        for x, y, expected in ((0, 0, "##\n##\n"),
                               (2, 1, "\n  ##\n  ##\n")):
            with self.subTest(x=x, y=y):
                output = StringIO()
                with redirect_stdout(output):
                    self.assertIsNone(Rectangle(2, 2, x, y, 1).display())
                self.assertEqual(output.getvalue(), expected)

    def test_update(self):
        """Apply partial updates and prefer positional arguments."""
        rect = Rectangle(2, 3, 4, 5, 6)
        rect.update()
        self.assertEqual(str(rect), "[Rectangle] (6) 4/5 - 2/3")
        rect.update(89, width=8)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/5 - 2/3")
        rect.update(90, 8, 9, 1, 2)
        self.assertEqual(str(rect), "[Rectangle] (90) 1/2 - 8/9")
        rect.update(y=3, height=1, id=0, x=2, width=4)
        self.assertEqual(str(rect), "[Rectangle] (0) 2/3 - 4/1")
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            rect.update(width=0)

    def test_dictionary(self):
        """Return a fresh dictionary usable as update arguments."""
        rect = Rectangle(5, 4, 3, 2, 1)
        fields = rect.to_dictionary()
        self.assertEqual(fields,
                         {"id": 1, "width": 5, "height": 4, "x": 3, "y": 2})
        other = Rectangle(1, 1, id=2)
        other.update(**fields)
        self.assertEqual(other.to_dictionary(), fields)
        fields["width"] = 20
        self.assertEqual(rect.width, 5)
