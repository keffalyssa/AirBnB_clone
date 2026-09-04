#!/usr/bin/python3
"""
Unittests for the City class.
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_inheritance(self):
        """Test that City inherits from BaseModel."""
        c = City()
        self.assertIsInstance(c, City)

    def test_attributes(self):
        """Test that City has required attributes."""
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertTrue(hasattr(c, "name"))


if __name__ == "__main__":
    unittest.main()
