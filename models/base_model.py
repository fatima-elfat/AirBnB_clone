#!/usr/bin/python3

"""
Defines the BaseModel class
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel
        """
        # deserializing **kwargs
        # **kwargs is a dictionary created from a basemodel instance
        if kwargs:
            for k, v in kwargs.items():
                # omitting '__class__' from deserialization
                if k != '__class__':
                    # Converting 'created_at', 'updated_at' to datetime objts
                    if k == 'created_at' or k == 'updated_at':
                        v = datetime.fromisoformat(v)
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return str of information of BaseModel.
        """
        return ('[{}] ({}) {}'.format(
            self.__class__.__name__,
            self.id, self.__dict__
            ))

    def save(self):
        """ Updates the public instance attribute
            updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        diction = {
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

        dict_copy = self.__dict__.copy()
        dict_copy.update(diction)
        return dict_copy
