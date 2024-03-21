#!/usr/bin/env python3
"""Unittest module for the Amenity Class."""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class TestAmenity(unittest.TestCase):
    """Amenity model class test case"""

    def setUp(self):
        """Instantiate the amenity class"""
        self.amenity = Amenity()
        self.amenity.name = "Netflix"

    def tearDown(self):
        """Delete the json file after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_if_subclass(self):
        """Test if Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

    def checking_for_doc(self):
        """Tests if Amenity module is documented."""
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """Test for attributes."""
        A = self.amenity
        self.assertTrue(hasattr(A, 'name'))
        self.assertTrue(hasattr(A, 'id'))
        self.assertTrue(hasattr(A, 'created_at'))
        self.assertTrue(hasattr(A, 'updated_at'))

    def test_attributes_type(self):
        """Test the attributes data type."""
        self.assertIs(type(self.amenity.name), str)

    def test_class_exists(self):
        """tests if class exists"""
        cls = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.amenity)), cls)

    def test_save(self):
        """Test if class instances are saved in json file."""
        self.amenity.save()
        A = self.amenity
        self.assertNotEqual(A.created_at, A.updated_at)

    def test_to_dict(self):
        """Test if to_dict method is implemented."""
        self.assertTrue('to_dict' in dir(self.amenity))


if __name__ == "__main__":
    unittest.main()
