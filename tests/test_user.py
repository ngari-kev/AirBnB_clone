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
        self.user1 = User()
        self.user1.email = "user1@mail.com"
        self.user1.password = "P$ssword"
        self.user1.first_name = "Foo"
        self.user1.last_name = "Bar"

    def tearDown(self):
        """Clean up the dirt"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_for_instantiation(self):
        """Tests instantiation of User class."""
        user1 = self.user1
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
        user = self.user1
        self.assertTrue('id' in user.__dict__)
        self.assertTrue('created_at' in user.__dict__)
        self.assertTrue('updated_at' in user.__dict__)
        self.assertTrue('email' in user.__dict__)
        self.assertTrue('password' in user.__dict__)
        self.assertTrue('first_name' in user.__dict__)
        self.assertTrue('last_name' in user.__dict__)

    def test_attribute_type(self):
        """Test data type of attributes."""
        user = self.user1
        self.assertIs(type(user.email), str)
        self.assertIs(type(user.password), str)
        self.assertIs(type(user.first_name), str)
        self.assertIs(type(user.last_name), str)

    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        user = self.user1
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def checking_for_doc(self):
        self.assertIsNotNone(User.__doc__)

    def test_save(self):
        """Tests if instance is saved."""
        user1 =self.user1
        user1.save()
        self.assertNotEqual(user1.created_at, user1.updated_at)

    def test_to_dict(self):
        """Test if method to_dict is available."""
        self.assertTrue('to_dict' in dir(self.user1))

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = self.user1
        new_dict = u.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in u.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = self.user1
        new_dict = u.to_dict()
        self.assertEqual(new_dict["__class__"], "User")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], u.created_at.strftime(time_format))
        self.assertEqual(new_dict["updated_at"], u.updated_at.strftime(time_format))


if __name__ == "__main__":
    unittest.main()    
