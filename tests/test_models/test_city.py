#!/usr/bin/python3
"""Unittests for the City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test the instantiation and attributes of the City class."""

    def test_is_subclass(self):
        """Test that City inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Test public class attributes of City."""
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def test_types(self):
        """Test attribute types."""
        c = City()
        self.assertIsInstance(c.state_id, str)
        self.assertIsInstance(c.name, str)


if __name__ == "__main__":
    unittest.main()
