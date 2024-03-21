#!/usr/bin/python3

"""Test file for the User module."""
import unittest
import os
from models import storage
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """This class tests the User class."""

    def setUp(self):
        """Sets up the unittest"""
        user1 = User()
        user1.email = "user1@mail.com"
        user1.password = "P$ssword"
        user1.first_name = "Foo"
        user1.last_name = "Bar"

    def test_for_instantiation(self):
        """Tests instantiation of User class."""
        user1 = User()
        self.assertEqual(str(type(user1)), "<class 'models.user.User'>")
        self.assertIsInstance(user1, User)
        self.assertTrue(issubclass(type(user1), BaseModel))

    def test_no_args_instantiates(self):
        """Tests if instance is created without args."""
        self.assertEqual(User, type(User()))

    def test_if_new_instance_stored(self):
        """Tests if instance is saved to json file."""
        self.assertIn(User(), storage.all().values())

    def test_id_is_public(self):
        """Tests if id class instance attribute is public."""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """Test if created_at class instance attribute is public."""
        self.assertEqual(datetime, type(User().created_at))

    def test_has_attributes(self):
        """Tests if User class has attributes."""
        user = User()
        self.assertTrue('id' in user.__dict__)
        self.assertTrue('created_at' in user.__dict__)
        self.assertTrue('updated_at' in user.__dict__)
        self.assertTrue('email' in user.__dict__)
        self.assertTrue('password' in user.__dict__)
        self.assertTrue('first_name' in user.__dict__)
        self.assertTrue('last_name' in user.__dict__)


if __name__ == "__main__":
    unittest.main()    
