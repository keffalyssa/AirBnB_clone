#!/usr/bin/python3
"""
Unittests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Setup test method."""
        self.bm = BaseModel()

    def test_init(self):
        """Test initialization and attributes."""
        self.assertIsInstance(self.bm, BaseModel)
        self.assertTrue(hasattr(self.bm, "id"))
        self.assertTrue(hasattr(self.bm, "created_at"))
        self.assertTrue(hasattr(self.bm, "updated_at"))

    def termDown(self):
        """Teardown method."""
        del self.bm

    def test_str(self):
        """Test __str__ output format."""
        string = str(self.bm)
        self.assertIn("[BaseModel]", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)

    def test_save(self):
        """Test save method updates updated_at."""
        old_updated = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(old_updated, self.bm.updated_at)

    def test_to_dict(self):
        """Test to_dict method dictionary keys."""
        bm_dict = self.bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertIsInstance(bm_dict["created_at"], str)
        self.assertIsInstance(bm_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
