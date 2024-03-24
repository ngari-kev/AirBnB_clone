#!/usr/bin/python3
"""Unittest module for State class."""
import pep8
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State
from models import storage
from models.base_model import BaseModel


class test_State(unittest.TestCase):
    """State class test case."""

    def setUp(self):
        """Instantiate the State class"""
        self.state1 = State()
        self.state1.name = "Texas"

    def tearDown(self):
        """Delete the json file after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_no_args_instantiates(self):
        """Tests if an instance can be created without arguments."""
        self.assertEqual(State, type(State()))

    def test_new_instance_stored(self):
        """Tests if new instances are stored in the json file."""
        self.assertIn(self.state1, models.storage.all().values())

    def test_id_is_public_str(self):
        """tests that the id attribute of the State instance is a string."""
        self.assertEqual(str, type(self.state1.id))

    def test_created_at_is_datetime(self):
        """Tests that the created_at attribute of the State
        instance is of type datetime."""
        self.assertEqual(datetime, type(self.state1.created_at))

    def test_updated_at_is_datetime(self):
        """Tests that the updated_at attribute of the State
        instance is of type datetime."""
        self.assertEqual(datetime, type(self.state1.updated_at))

    def test_name_is_class_attribute(self):
        """Tests that the name attribute is accessible as a class attribute
        (State.name) but not as an instance attribute (state1.name)."""
        st = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(st))
        self.assertNotIn("name", st.__dict__)

    def test_unique_ids(self):
        """test that two different instances have unique id attributes."""
        state2 = State()
        self.assertNotEqual(self.state1.id, state2.id)

    def test_created_at(self):
        """Tests that the created_at timestamp of the 2nd instance is greater
        than the created_at timestamp of the 1st instance."""
        self.state1
        sleep(0.05)
        state2 = State()
        self.assertLess(self.state1.created_at, state2.created_at)

    def test_updated_at(self):
        """Tests hat the updated_at timestamp of the 2nd instance is greater
        than the updated_at timestamp of the 1st instance."""
        self.state1
        sleep(0.05)
        st2 = State()
        self.assertLess(self.state1.updated_at, st2.updated_at)

    def test_str(self):
        """Tests if the string representation of a State instance contains the
        expected information, including its id, created_at, and updated_at
        attributes."""
        dt = datetime.today()
        dt_repr = repr(dt)
        st = State()
        st.id = "123456"
        st.created_at = st.updated_at = dt
        ststr = st.__str__()
        self.assertIn("[State] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'created_at': " + dt_repr, ststr)
        self.assertIn("'updated_at': " + dt_repr, ststr)

    def test_args_None(self):
        """ test verifies that passing None as an argument when instantiating
        an instance doesn't result in any None
        values being stored in the instance's __dict__."""
        st = State(None)
        self.assertNotIn(None, st.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """test checks if a State instance can be instantiated using keyword
        arguments for id, created_at, and updated_at."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        st = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(st.id, "345")
        self.assertEqual(st.created_at, dt)
        self.assertEqual(st.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test verifies that instantiating a State instance with None"""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/state.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
