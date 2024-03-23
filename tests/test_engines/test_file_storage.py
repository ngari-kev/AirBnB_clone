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

    def tearDownClass(cls):
        """Clean up the dirt"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_save_and_reload(self):
        """Adds objects to storage, reloads and tests if they were created."""
        self.storage.new(BaseModel())
        self.storage.new(BaseModel())
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertEqual(len(new_storage.all()), 2)

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
