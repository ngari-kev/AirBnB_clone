#!/usr/bin/python3
"""Tests for FileStorage module."""

import unittest
import os
from os import path
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import json
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage module."""
    def setUp(self):
        """Instantiates an instance of FileStorage class."""
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up the dirt"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_initialization(self):
        """Tests if instances and files have been created."""
        self.assertIsInstance(self.storage, FileStorage)
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_new(self):
        """Test new() method."""
        obj = BaseModel()
        self.storage.new(obj)

        self.assertIn(obj.__class__.__name__ + "." + obj.id,
                      self.storage.all())

    def test_all(self):
        """ Tests all() method."""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new_empty(self):
        """tests new() method """
        with self.assertRaises(TypeError):
            storage.new()

    def test_reload(self):
        """ tests  reload() method. """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User()
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City()
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity()
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place()
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review()
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State()
        obj6_key = 'State' + '.' + obj6.id
        storage.save()

        self.assertTrue(path.isfile('file.json'))
        FileStorage._FileStorage__objects = {}

        storage.reload()

        self.assertTrue(obj_key in storage.all().keys())
        self.assertEqual(obj.id, storage.all()[obj_key].id)
        self.assertTrue(obj1_key in storage.all().keys())
        self.assertEqual(obj1.id, storage.all()[obj1_key].id)
        self.assertTrue(obj2_key in storage.all().keys())
        self.assertEqual(obj2.id, storage.all()[obj2_key].id)
        self.assertTrue(obj3_key in storage.all().keys())
        self.assertEqual(obj3.id, storage.all()[obj3_key].id)
        self.assertTrue(obj4_key in storage.all().keys())
        self.assertEqual(obj4.id, storage.all()[obj4_key].id)
        self.assertTrue(obj5_key in storage.all().keys())
        self.assertEqual(obj5.id, storage.all()[obj5_key].id)
        self.assertTrue(obj6_key in storage.all().keys())
        self.assertEqual(obj6.id, storage.all()[obj6_key].id)


if __name__ == '__main__':
    unittest.main()
