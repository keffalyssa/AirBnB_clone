#!/usr/bin/python3
"""Unittests for the State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test the instantiation and attributes of the State class."""

    def test_is_subclass(self):
        """Test that State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Test public class attributes of State."""
        self.assertTrue(hasattr(State, "name"))
        self.assertEqual(State.name, "")

    def test_types(self):
        """Test attribute types."""
        s = State()
        self.assertIsInstance(s.name, str)


if __name__ == "__main__":
    unittest.main()
