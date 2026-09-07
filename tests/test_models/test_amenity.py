#!/usr/bin/python3
"""Unittests for the Amenity class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test the instantiation and attributes of the Amenity class."""

    def test_is_subclass(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Test public class attributes of Amenity."""
        self.assertTrue(hasattr(Amenity, "name"))
        self.assertEqual(Amenity.name, "")

    def test_types(self):
        """Test attribute types."""
        a = Amenity()
        self.assertIsInstance(a.name, str)


if __name__ == "__main__":
    unittest.main()
