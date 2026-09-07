#!/usr/bin/python3
"""Unittests for the Place class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test the instantiation and attributes of the Place class."""

    def test_is_subclass(self):
        """Test that Place inherits from BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """Test public class attributes of Place."""
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

    def test_types(self):
        """Test attribute types."""
        p = Place()
        self.assertIsInstance(p.city_id, str)
        self.assertIsInstance(p.user_id, str)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.description, str)
        self.assertIsInstance(p.number_rooms, int)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.max_guest, int)
        self.assertIsInstance(p.price_by_night, int)
        self.assertIsInstance(p.latitude, float)
        self.assertIsInstance(p.longitude, float)
        self.assertIsInstance(p.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
