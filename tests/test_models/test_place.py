#!/usr/bin/python3
"""
Unittests for the Place class.
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_inheritance(self):
        """Test that Place inherits from BaseModel."""
        p = Place()
        self.assertIsInstance(p, Place)

    def test_attributes(self):
        """Test that Place has required attributes."""
        p = Place()
        self.assertTrue(hasattr(p, "city_id"))
        self.assertTrue(hasattr(p, "user_id"))
        self.assertTrue(hasattr(p, "name"))
        self.assertTrue(hasattr(p, "description"))
        self.assertTrue(hasattr(p, "number_rooms"))
        self.assertTrue(hasattr(p, "number_bathrooms"))
        self.assertTrue(hasattr(p, "max_guest"))
        self.assertTrue(hasattr(p, "price_by_night"))
        self.assertTrue(hasattr(p, "latitude"))
        self.assertTrue(hasattr(p, "longitude"))
        self.assertTrue(hasattr(p, "amenity_ids"))


if __name__ == "__main__":
    unittest.main()
