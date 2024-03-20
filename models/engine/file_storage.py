#!/usr/bin/python3
"""
This is a module that deals with serializing and deserializing
to and from JSON files respectively.
"""

from os import path
import json
from models.base_model import BaseModel

class FileStorage():
    """
    It serializes instances to a JSON file and deserializes
    JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return:
            the dictionary object.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with a key.

        Args:
            obj - Object to be added to __objects.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to a JSON file.
        """
        serialized = {key: obj.to_dict()
                      for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(serialized, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                serialized = json.load(f)
                for key, object_dict in serialized.items():
                    FileStorage.__objects[key] = eval(
                        object_dict['__class__'])(**object_dict) 
