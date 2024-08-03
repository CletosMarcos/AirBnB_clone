#!/usr/bin/python3
"""This module defines the Base Class"""

from datetime import datetime
import uuid


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self. id}) {self.__dict__}"

    def save(self):
        """updates instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
            of __dict__ of the instance"""

        self.__dict__["__class__"] = self.__class__.__name__

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()

        return self.__dict__
