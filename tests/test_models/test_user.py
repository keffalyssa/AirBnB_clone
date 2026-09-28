#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_is_subclass(self):
        """Check that User is a subclass of BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Check that User has the correct attributes and default values."""
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_types(self):
        """Check types of User attributes."""
        u = User()
        self.assertIsInstance(u.email, str)
        self.assertIsInstance(u.password, str)
        self.assertIsInstance(u.first_name, str)
        self.assertIsInstance(u.last_name, str)
        self.assertIsInstance(u.id, str)


if __name__ == "__main__":
    unittest.main()
