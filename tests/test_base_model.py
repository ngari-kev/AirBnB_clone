#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import re
import uuid
"""
This is a unittest for base_model.py
"""


class TestBaseModel(unittest.TestCase):
    """
    This tests the existance of the BaseModel class.
    """

    def setUp(self):
        """
        Instanciates a class instance of the BaseModel class.
        """
        self.test = BaseModel()
        self.test2 = BaseModel()

    def test_attributes(self):
        """
        Checks and tests the existance of attributes in the class.
        """
        self.assertTrue(hasattr(self.test, 'id'))
        self.assertTrue(hasattr(self.test, 'created_at'))
        self.assertTrue(hasattr(self.test, 'updated_at'))
        self.assertIsInstance(self.test.created_at, datetime)
        self.assertIsInstance(self.test.updated_at, datetime)
        self.assertIsInstance(self.test.id, str)

    def test_save(self):
        """
        Checks for the save method.
        """
        updated_at = self.test.updated_at
        self.test.save()
        self.assertNotEqual(updated_at, self.test.updated_at)

    def test_IdType(self):
        """Test if `id` attribute type"""
        b1 = self.test
        self.assertEqual(type(b1.id), str)

    def test_CompareTwoInstancesId(self):
        """Compare distinct instances ids"""
        b1 = self.test
        b2 = self.test2
        self.assertNotEqual(b1.id, b2.id)

    def test_uuid(self):
        """Test that id is a valid uuid"""
        b1 = BaseModel()
        b2 = BaseModel()
        for inst in [b1, b2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(b1.id, b2.id)

    def test_uniq_id(self):
        """Tests for unique user ids."""
        u = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(u)), len(u))

    def test_datetime_created(self):
        """Tests if updated_at & created_at are current at creation."""
        date_now = datetime.now()
        b1 = self.test
        diff = b1.updated_at - b1.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = b1.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_to_dict(self):
        """
        Checks for the dict method.
        """
        o_dict = self.test.to_dict()
        self.assertTrue('__class__' in o_dict)
        self.assertEqual(o_dict['__class__'],  'BaseModel')
        self.assertTrue('id' in o_dict)
        self.assertTrue('created_at' in o_dict)
        self.assertTrue('updated_at' in o_dict)
        self.assertIsInstance(o_dict['created_at'], str)
        self.assertIsInstance(o_dict['updated_at'], str)

    def test_str(self):
        """
        Checks for str method
        """
        cls_name = self.test.__class__.__name__
        expected_str = "[{}] ({}) {}".format(cls_name, self.test.id, self.test.__dict__)
        self.assertEqual(str(self.test), expected_str)

    def test_for_classname(self):
        """Test if classname is present."""
        dictionary = self.test.to_dict()
        self.assertNotEqual(dictionary, self.test.__dict__)

    def test_if_in_ISO_format(self):
        """Test if datetime value is isoformated."""
        dictionary = self.test.to_dict()
        self.assertEqual(type(dictionary['created_at']), str)
        self.assertEqual(type(dictionary['updated_at']), str)

    def test_to_dict_type(self):
        """Test for the dictionary type."""
        self.assertTrue(dict, type(self.test.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test for correct KeyValue pair in dictionary."""
        b1 = self.test
        self.assertIn("id", b1.to_dict())
        self.assertIn("created_at", b1.to_dict())
        self.assertIn("updated_at", b1.to_dict())
        self.assertIn("__class__", b1.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if dict contains the added attributes."""
        b1 = self.test
        b1.name = "Eske"
        b1.my_number = 1008
        self.assertIn("name", b1.to_dict())
        self.assertIn("my_number", b1.to_dict())

    def test_to_dict_output(self):
        """Test the output of the to_dict method."""
        dt = datetime.now()
        b1 = self.test
        b1.id = "123456"
        b1.created_at = b1.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(b1.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test for equality in __dict__ and to_dict."""
        b1 = self.test
        self.assertNotEqual(b1.to_dict(), b1.__dict__)

    def test_to_dict_with_arg(self):
        """Test if args are passed instead of kwargs."""
        b1 = self.test
        with self.assertRaises(TypeError):
            b1.to_dict(None)

if __name__ == '__main__':
    unittest.main()
