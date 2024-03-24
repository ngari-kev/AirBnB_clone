#!/usr/bin/python3
"""Tests for FileStorage module."""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import json
from models import storage
import os


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

    def test_new_method(self):
        """Adds a new object and tests if added to storage."""
        obj = BaseModel()
        self.storage.new(obj)

        self.assertIn(obj.__class__.__name__ + "." + obj.id,
                      self.storage.all())


if __name__ == '__main__':
    unittest.main()
