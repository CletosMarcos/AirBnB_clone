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
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
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

        if os.path.exists(FileStorage.__file_path):
            classes = {"BaseModel": BaseModel}
            with open(FileStorage.__file_path) as f:
                temp = {}
                temp = json.load(f)
                for k, v in temp.items():
                    name = v["__class__"]
                    FileStorage.__objects[k] = classes[name](**v)
