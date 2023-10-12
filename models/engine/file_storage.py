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
    __file_path = "file.json" # path to JSON file
    __objects = {} # will store objects(<class name>.id)

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects 
    
    def new(self, obj):
        """Populates __objects with <obj class name>.obj as key"""
        self.__objects[obj.__class__.__name__+ '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as file:
            for k,v in self.__objects.items():
                    temp_dict = {}
                    temp_dict[k] = v
            json.dump(temp_dict, file)
    
    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path) as file:
                    return json.load(file)
        except:
            pass