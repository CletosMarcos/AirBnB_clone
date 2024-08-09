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
        temp = {}
        for k, v in FileStorage.__objects.items():
            temp[k] = v.__dict__
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(temp))

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = json.load(f)
        else:
            pass
