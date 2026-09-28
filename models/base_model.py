#!/usr/bin/python3
"""Defines the BaseModel class."""
from datetime import datetime
import uuid


class BaseModel:
    """Represents the BaseModel of the AirBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            import models
            models.storage.new(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime and save to storage."""
        self.updated_at = datetime.now()
        import models
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return the dictionary representation of the BaseModel instance."""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
