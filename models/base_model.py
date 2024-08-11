#!/usr/bin/python3
"""This module defines the Base Class"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """initializes instance attributes
        if kwargs is passed, an object is reloaded
        else, create a new one"""
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at":
                        v = datetime.fromisoformat(v)
                    elif k == "updated_at":
                        v = datetime.fromisoformat(v)
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            storage.new(self)

    def __str__(self):
        """Returns a tring representation of the instance"""
        return f"[{self.__class__.__name__}] ({self. id}) {self.__dict__}"

    def save(self):
        """updates instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        # save instance to json file
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
            of __dict__ of the instance"""

        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__

        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
