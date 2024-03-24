#!/usr/bin/python3
"""Defines unittests for the console module."""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class test_console(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        """Tests the prompting string."""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """Tests emptyline method."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_help_quit(self):
        """Test help_quit method."""
        h = "Quit command Exits the console."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_create(self):
        """Tests help_create method."""
        h = ("Creates an instance based on class name only"
             "\nUsage: create <classname>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_EOF(self):
        """Tests for help_EOF method."""
        h = "EOF command exits the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_show(self):
        """Tests for help_show method."""
        h = ("Prints the string representation of an instance based on the "
             "class name and id.\nUsage: show <class name> <id>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_destroy(self):
        """Tests for help_destroy method."""
        h = ("Deletes an instance based on the class name and id (save the "
             "change into the JSON file). \nUsage: destroy <class name> <id>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_all(self):
        """Tests for help_all method."""
        h = ("Prints all string representation of all instances based "
             "or not on the class name.\nUsage: all OR all <class name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_count(self):
        """Tests for help_count method."""
        h = ("Retrieves the number of instances of a class"
             "\nUsage: <class name>.count()")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_update(self):
        """Tests for help_update method."""
        h = ("Updates an instance based on the class name and id by adding or"
             " updating attribute (save the change into the JSON file)\nUsage"
             ": update <class name> <id> <attribute name>, attribute value>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help(self):
        h = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
