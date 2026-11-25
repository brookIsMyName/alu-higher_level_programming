#!/usr/bin/python3
"""Test instance IDs and JSON persistence for the model classes."""
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Exercise identifiers and JSON operations through public methods."""

    def setUp(self):
        """Isolate the ID counter and file operations for each test."""
        counter = Base._Base__nb_objects
        self.addCleanup(setattr, Base, "_Base__nb_objects", counter)
        Base._Base__nb_objects = 0
        workspace = TemporaryDirectory()
        self.addCleanup(workspace.cleanup)
        self.addCleanup(os.chdir, os.getcwd())
        os.chdir(workspace.name)

    def test_ids(self):
        """Share automatic IDs across classes and preserve explicit IDs."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Rectangle(2, 3).id, 2)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Square(2, id=-7).id, -7)
        self.assertEqual(Square(1).id, 3)
        self.assertEqual(Base(None).id, 4)

    def test_to_json_string(self):
        """Serialize empty and populated input as JSON strings."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        data = [{"id": 8, "width": 2}, {"id": 9, "size": 5}]
        result = Base.to_json_string(data)
        self.assertIsInstance(result, str)
        self.assertEqual(json.loads(result), data)

    def test_update_with_none_id(self):
        """Allocate a new ID on update and retain the shape's geometry."""
        rect = Rectangle(3, 4, 2, 1, 18)
        square = Square(5, 1, 2, 19)
        rect.update(None)
        square.update(id=None)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/1 - 3/4")
        self.assertEqual(str(square), "[Square] (2) 1/2 - 5")
        self.assertEqual(Base().id, 3)

    def test_from_json_string(self):
        """Decode JSON, including an absent or empty value."""
        for value in (None, "", "[]"):
            with self.subTest(value=value):
                self.assertEqual(Base.from_json_string(value), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])

    def test_save_overwrites_and_uses_class_name(self):
        """Write fresh JSON for each concrete class and handle empty input."""
        rect = Rectangle(3, 4, 2, 1, 12)
        square = Square(2, 3, 1, 15)
        Rectangle.save_to_file([rect])
        Square.save_to_file([square])
        self.assertEqual(json.loads(Path("Rectangle.json").read_text()),
                         [rect.to_dictionary()])
        self.assertEqual(json.loads(Path("Square.json").read_text()),
                         [square.to_dictionary()])
        Rectangle.save_to_file(None)
        Square.save_to_file([])
        self.assertEqual(Path("Rectangle.json").read_text(), "[]")
        self.assertEqual(Path("Square.json").read_text(), "[]")

    def test_create(self):
        """Rebuild each concrete model as a distinct validated instance."""
        originals = (Rectangle(3, 5, 1, 2, 10), Square(7, 3, 2, 11))
        for original in originals:
            with self.subTest(model=type(original)):
                fields = original.to_dictionary()
                instance = type(original).create(**fields)
                self.assertIs(type(instance), type(original))
                self.assertIsNot(instance, original)
                self.assertEqual(instance.to_dictionary(), fields)
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            Rectangle.create(width=0)

    def test_load_from_file(self):
        """Handle missing files and round-trip ordered model collections."""
        cases = (
            (Rectangle, [Rectangle(2, 3), Rectangle(4, 1, 2, 3)]),
            (Square, [Square(2), Square(5, 3, 2)]),
        )
        for model, originals in cases:
            with self.subTest(model=model):
                self.assertEqual(model.load_from_file(), [])
                model.save_to_file(originals)
                objects = model.load_from_file()
                self.assertEqual(len(objects), len(originals))
                for actual, original in zip(objects, originals):
                    self.assertIs(type(actual), model)
                    self.assertIsNot(actual, original)
                    self.assertEqual(actual.to_dictionary(),
                                     original.to_dictionary())
                model.save_to_file([])
                self.assertEqual(model.load_from_file(), [])
