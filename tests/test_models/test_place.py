#!/usr/bin/env python3
"""Test for Place module"""

import pep8
import unittest
import os
from models.place import Place
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
import uuid


class TestPlace(unittest.TestCase):
    """Place model class test case"""

    def setUp(self):
        """Setup the unittest"""
        self.place = Place()
        self.place.city_id = str(uuid.uuid4())
        self.place.user_id = str(uuid.uuid4())
        self.place.name = "Nairobi"
        self.place.description = "In the capital city"
        self.place.number_rooms = 1
        self.place.number_bathrooms = 1
        self.place.max_guest = 2
        self.place.price_by_night = 2500
        self.place.latitude = 0.0
        self.place.longitude = 0.0
        self.place.amenity_ids = []

    def tearDown(self):
        """Clean up the dirt"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """Test that Place iherits from BaseModel."""
        self.assertTrue(issubclass(self.place.__class__, BaseModel))

    def test_doc(self):
        """Test for documentation."""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes(self):
        """Test for attributes."""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)

    def test_attributes_are_string(self):
        """Tests the type of attributes."""
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

    def test_save(self):
        """Test that when save() is called on Place, updated_at attr changes"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_save_1(self):
        """Tests that updated_at attr changes with each call."""
        self.place
        sleep(0.05)
        first_updated_at = self.place.updated_at
        self.place.save()
        self.assertLess(first_updated_at, self.place.updated_at)

    def test_save_2(self):
        """Tests that updated_at changes after calling save() twice."""
        self.place
        sleep(0.05)
        first_updated_at = self.place.updated_at
        self.place.save()
        second_updated_at = self.place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        self.place.save()
        self.assertLess(second_updated_at, self.place.updated_at)

    def test_save_with_arg(self):
        """Tests if save takes an argument."""
        with self.assertRaises(TypeError):
            self.place.save(None)

    def test_to_dict_type(self):
        """Test return value of to_dict() is a dictionary."""
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_keys(self):
        """Tests  that the dictionary returned by to_dict() contains the
        correct keys: "id", "created_at", "updated_at", and "__class__"."""
        self.assertIn("id", self.place.to_dict())
        self.assertIn("created_at", self.place.to_dict())
        self.assertIn("updated_at", self.place.to_dict())
        self.assertIn("__class__", self.place.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Tests if attributes are stored in the dictionary returned."""
        self.place.middle_name = "Holberton"
        self.place.my_number = 98
        self.assertEqual("Holberton", self.place.middle_name)
        self.assertIn("my_number", self.place.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        pl_dict = self.place.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        self.place = Place()
        dt = datetime.today()
        self.place.id = "573456"
        self.place.created_at = self.place.updated_at = dt
        tdict = {
            'id': '573456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(self.place.to_dict(), tdict)

    def test_to_dict_and_dunder_dict(self):
        """Tests that the dictionary returned by to_dict() is different from
        the instance's __dict__."""
        self.assertNotEqual(self.place.to_dict(), self.place.__dict__)

    def test_to_dict_with_arg(self):
        """Tests if calling to_dict() with an argument raises a TypeError"""
        with self.assertRaises(TypeError):
            self.place.to_dict(None)

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/place.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
