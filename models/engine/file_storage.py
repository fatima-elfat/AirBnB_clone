#!/usr/bin/python3

"""
Defines the FileStorage class: serializes instances to a JSON file
and deserializes JSON file to instances:
"""

import json
import os
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        object_value = obj.__class__.__name__+ '.' + obj.id
        self.__objects[object_value] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as file:
            temp_dict = {}
            for k,v in self.__objects.items():   
                temp_dict[k] = v.to_dict()
            json.dump(temp_dict, file)
    
    def reload(self):
        """Deserializes the JSON file to __objects"""
        from_json = {}
        try:
            with open(self.__file_path, mode='r', encoding="UTF-8") as myfile:
                from_json = json.load(myfile)      # saves dic in variable
                for key, value in from_json.items():   # iterates through key and value of dictionary
                    attr_cls_name = value.pop("__class__")  # removes from the dict,the value of __class__, 'BaseModel' and assigns it to attr_cls_name
                    self.new(eval(attr_cls_name)(**value))  # self.new(BaseModel(**value)). Recreates the BaseModel object and passes it to new()
        except:
            pass