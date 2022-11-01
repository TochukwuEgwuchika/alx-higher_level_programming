#!/usr/bin/python3
"""
Contains the base class
"""

import json

class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        objs = []
        with open("{}.json".format(cls.__name__), "w") as f:
            if list_objs is not None:
                for obj in list_objs:
                    objs.append(cls.to_dictionary(obj))
            f.write(cls.to_json_string(objs))

