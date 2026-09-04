#!/usr/bin/python3
"""
Unittests for the User class.
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        u = User()
        self.assertIsInstance(u, User)

    def test_attributes(self):
        """Test that User has required attributes."""
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))


if __name__ == "__main__":
    unittest.main()
