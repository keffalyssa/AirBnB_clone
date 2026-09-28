#!/usr/bin/python3
"""Unittests for the Review class."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test the instantiation and attributes of the Review class."""

    def test_is_subclass(self):
        """Test that Review inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """Test public class attributes of Review."""
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

    def test_types(self):
        """Test attribute types."""
        r = Review()
        self.assertIsInstance(r.place_id, str)
        self.assertIsInstance(r.user_id, str)
        self.assertIsInstance(r.text, str)


if __name__ == "__main__":
    unittest.main()
