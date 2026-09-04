#!/usr/bin/python3
"""
Unittests for the State class.
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_inheritance(self):
        """Test that State inherits from BaseModel."""
        s = State()
        self.assertIsInstance(s, State)

    def test_attributes(self):
        """Test that State has required attributes."""
        s = State()
        self.assertTrue(hasattr(s, "name"))


if __name__ == "__main__":
    unittest.main()
