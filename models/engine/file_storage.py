#!/usr/bin/python3
"""
the model of FileStorage.
It serializes instances to a
JSON file and deserializes JSON file to instances:
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    class of FileStorage.
    Attributes:
        __file_path (str): string - path to the JSON
            file (ex: file.json).
        __objects (dict): dictionary - empty but will store all objects
            by <class name>.id (ex: to store a BaseModel object
            with id=121, the key will be BaseModel.121)
    """
    __file_path = "file.json"
    __objects = {}
    clss = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

    def all(self):
        """
        returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id.
        Args:
            obj (instance): of object to add to objects.
        """
        i = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[i] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path).
        """
        dump_dict = {}
        for key, val in FileStorage.__objects.items():
            dump_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dump_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects.
        if FileNotFoundError no exception should be raised.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                the_dict = json.load(f)
                for key, val in the_dict.items():
                    r = FileStorage.clss[val['__class__']](**val)
                    FileStorage.__objects[key] = r
        except FileNotFoundError:
            pass
