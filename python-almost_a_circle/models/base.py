#!/usr/bin/python3
"""Manage shared model identifiers and JSON persistence."""
import json


class Base:
    """Provide automatic identifiers and serialization for shape models."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Use an explicit identifier or allocate the next automatic one."""
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize a list of dictionaries, treating None as an empty list."""
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """Overwrite the class's JSON file with the given model objects."""
        dictionaries = [obj.to_dictionary() for obj in (list_objs or [])]
        data = cls.to_json_string(dictionaries)
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as file:
            file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """Decode a JSON list or return an empty list for absent input."""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """Build a shape with temporary dimensions and apply its fields."""
        from models.square import Square

        if issubclass(cls, Square):
            instance = cls(1)
        else:
            instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Load new instances from the class's JSON file when it exists."""
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as file:
                dictionaries = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []
        return [cls.create(**fields) for fields in dictionaries]
