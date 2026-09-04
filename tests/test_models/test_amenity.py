#!/usr/bin/python3
"""
Unittests for the Amenity class.
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel."""
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_attributes(self):
        """Test that Amenity has required attributes."""
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))


if __name__ == "__main__":
    unittest.main()
