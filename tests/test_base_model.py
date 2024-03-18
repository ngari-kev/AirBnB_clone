import unittest
from models.base_model import BaseModel
from datetime import datetime
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

if __name__ == '__main__':
    unittest.main()
