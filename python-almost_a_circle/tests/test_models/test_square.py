#!/usr/bin/python3
"""Test square behavior and its use of inherited rectangle operations."""
from contextlib import redirect_stdout
from io import StringIO
import unittest

from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Check the square's geometry, validation, display, and updates."""

    def test_constructor_and_display(self):
        """Use equal dimensions and render a square with the given offsets."""
        square = Square(2, 1, 1, 3)
        self.assertIsInstance(square, Rectangle)
        self.assertEqual((square.size, square.width, square.height), (2, 2, 2))
        self.assertEqual(str(square), "[Square] (3) 1/1 - 2")
        self.assertEqual(square.area(), 4)
        output = StringIO()
        with redirect_stdout(output):
            square.display()
        self.assertEqual(output.getvalue(), "\n ##\n ##\n")

    def test_invalid_construction(self):
        """Use inherited width and offset validation for square arguments."""
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaisesRegex(TypeError, "^width must be an integer$"):
            Square(3.0)
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "^x must be >= 0$"):
            Square(3, x=-1)
        with self.assertRaisesRegex(TypeError, "^y must be an integer$"):
            Square(3, y=None)

    def test_size_setter(self):
        """Resize both dimensions and reject invalid sizes consistently."""
        square = Square(3, id=5)
        square.size = 7
        self.assertEqual((square.size, square.width, square.height), (7, 7, 7))
        self.assertEqual(square.area(), 49)
        with self.assertRaisesRegex(TypeError, "^width must be an integer$"):
            square.size = "8"
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            square.size = -1
        self.assertEqual(square.size, 7)

    def test_update(self):
        """Set square-specific fields and give positional updates priority."""
        square = Square(2, 1, 3, 4)
        square.update()
        self.assertEqual(str(square), "[Square] (4) 1/3 - 2")
        square.update(8, size=5, x=7)
        self.assertEqual(str(square), "[Square] (8) 1/3 - 2")
        square.update(9, 6, 2, 1)
        self.assertEqual(str(square), "[Square] (9) 2/1 - 6")
        square.update(size=8, y=3, id=0, x=5)
        self.assertEqual(str(square), "[Square] (0) 5/3 - 8")
        self.assertEqual(square.area(), 64)
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            square.update(size=0)

    def test_dictionary(self):
        """Represent a square with its size, ID, and offsets."""
        square = Square(4, 2, 3, 1)
        dictionary = square.to_dictionary()
        self.assertEqual(dictionary, {"id": 1, "size": 4, "x": 2, "y": 3})
        other = Square(1, id=2)
        other.update(**dictionary)
        self.assertEqual(other.to_dictionary(), dictionary)
        dictionary["size"] = 20
        self.assertEqual(square.size, 4)
