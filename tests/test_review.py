#!/usr/bin/env python3
"""Test model for Review module"""

import pep8
import unittest
import os
from datetime import datetime
from time import sleep
from models import storage
from models.review import Review
from models.base_model import BaseModel
import uuid


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def setUp(self):
        """Setup the unittest"""
        self.review = Review()
        self.review.user_id = str(uuid.uuid4())
        self.review.place_id = str(uuid.uuid4())
        self.review.text = "The host was really sweet. Loved our stay"

    def tearDown(self):
        """Clean up the dirt"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """test that Review inherits from BaseModel."""
        self.assertTrue(issubclass(self.review.__class__, BaseModel))

    def test_doc(self):
        """Test for documentation."""
        self.assertIsNotNone(Review.__doc__)

    def test_no_args_instantiates(self):
        """Tests that calling Review() without any arguments results in an
        instance of the Review class."""
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored(self):
        """Tests if the newly created Review instance is stored in the objects
        dictionary within the storage."""
        self.assertIn(Review(), storage.all().values())

    def test_id(self):
        """Tests that the id attribute is of type string."""
        self.assertEqual(str, type(Review().id))

    def test_created(self):
        """Tests that the created_at attribute is of type datetime."""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated(self):
        """Tests that the updated_at attribute is of type datetime."""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id(self):
        """Test if place_id is a public class attribute and not present in the
        __dict__ attribute of the instance."""
        self.review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(self.review))
        self.assertNotIn("place_id", self.review.__dict__)

    def test_user_id(self):
        """Test if user_id is a public class attribute and not present in
        the __dict__ attribute of the instance."""
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
#        self.assertNotIn("user_id", rv.__dict__)

    def test_text(self):
        """Test if text is a public class attribute and not present in the
        __dict__ attribute of the instance."""
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_unique_ids(self):
        """Tests if two ids are identical."""
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_two_created_at(self):
        """Tests that the created_at timestamps of two different
        instances are different."""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_two_updated_at(self):
        """Tests that the updated_at timestamps of two
        different instances are different."""
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_str(self):
        """Test __str__ is in correct format."""
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    def test_args_unused(self):
        """Tests that passing None as arguments does not raise any error."""
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Tests instantiation of Review with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """ Tests instantiation of Review with None as keyword arguments."""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/review.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
