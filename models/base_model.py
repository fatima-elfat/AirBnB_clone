#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Initializes a new BaseModel
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the class
        """
        return f"{[self.__class__.__name__]} ({self.id}) {str(self.__dict__)}"

    def save(self):
        """ Updates the public instance attribute
            updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        diction = {
            "__class__": self.__class.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

        dict_copy = self.__dict__.copy()
        dict_copy.update(diction)
        return dict_copy
