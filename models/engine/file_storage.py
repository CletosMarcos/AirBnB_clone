#!/usr/bin/python3
"""Module that deals with Serialization and Deserialization"""

import json
import os


class FileStorage:
    """
        serializes instances to a JSON file and deserializes
        JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}  # store all objects by <class name>.id

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        in other words
        Adds new object to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        temp = FileStorage.__objects.copy()
        for k, v in temp.items():
            temp[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(temp, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        if os.path.exists(FileStorage.__file_path):
            classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
                       "State": State, "City": City,
                       "Amenity": Amenity, "Review": Review}
            with open(FileStorage.__file_path) as f:
                temp = {}
                temp = json.load(f)
                for k, v in temp.items():
                    name = v["__class__"]
                    FileStorage.__objects[k] = classes[name](**v)
