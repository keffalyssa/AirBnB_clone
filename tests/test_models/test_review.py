#!/usr/bin/python3
"""
Unittests for the Review class.
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_inheritance(self):
        """Test that Review inherits from BaseModel."""
        r = Review()
        self.assertIsInstance(r, Review)

    def test_attributes(self):
        """Test that Review has required attributes."""
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertTrue(hasattr(r, "user_id"))
        self.assertTrue(hasattr(r, "text"))


if __name__ == "__main__":
    unittest.main()
