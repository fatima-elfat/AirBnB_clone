#!/usr/bin/python3

"""
Defines the FileStorage class: serializes instances to a JSON file
and deserializes JSON file to instances:
"""

import json
import os


class FileStorage():
    """Serializes instances to a JSON file
        and deserializes JSON file to instances
    """
    __file_path = "" # path to JSON file
    __objects = {} # will store objects(<class name>.id)

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects 
    
    def new(self, obj):
        """Populates __objects with <obj class name> as key"""
        FileStorage.__objects[obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)
    
    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path) as file:
                    return json.load(file)
        except:
            pass