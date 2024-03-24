#!/usr/bin/python3
"""Unittest module for the City Class."""

import pep8
import unittest
from datetime import datetime
import time
import uuid
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """City model class test case"""

    def setUp(self):
        """Setup the unittest"""
        self.city = City()
        self.city.state_id = str(uuid.uuid4())
        self.city.name = "St. Petesburg"

    def tearDown(self):
        """Clean up the dirt"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_no_args(self):
        """Tests for when you instantiate a City object with no args."""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """tests that new instances are stored in json file."""
        self.assertIn(City(), storage.all().values())

    def test_id(self):
        """Tests that id attribute is a string."""
        self.assertEqual(str, type(City().id))

    def test_created_at(self):
        """Tests that the created_at attribute is a datetime object."""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at(self):
        """Tests that updated_at attribute is a datetime object."""
        self.assertEqual(datetime, type(City().updated_at))

    def test_is_subclass(self):
        """Tests if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def test_doc(self):
        """Tests if City class has a docstring."""
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        """Tests for attributes."""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_attributes_are_string(self):
        """Tests that attributes of class City are strings."""
        self.assertIs(type(self.city.state_id), str)
        self.assertIs(type(self.city.name), str)

    def test_save(self):
        """Tests that updated_at changes after saving."""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Tests if the to_dict() method is present in the City class."""
        self.assertTrue('to_dict' in dir(self.city))

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/city.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
