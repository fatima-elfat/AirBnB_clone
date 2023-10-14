#!/usr/bin/python3
"""
module of the BaseModel.
A parent class, to take care of the initialization,
serialization and deserialization of your future
instances.
"""


import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    BaseModel Class

    Attributes:
        id (str) : a value which is unique for
            each instance.
        created_at (datetime) : the current datetime when
            an instance is created.
        updated_at (datetime) : the current datetime when
            an instance is created and it will be
            updated every time you change your object.

    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new object.

        Args:
            *args (any): a list of the unknown arguments.
            **kwargs (dict): the name of the attr and their
                values (Key/value).

        """
        iso_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(
                        val,
                        iso_format
                        )
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
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
        """
        updates the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        create a dictionary representation
        with “simple object type”.
        Returns: a dictionary of all keys/values of __dict__ .
        """
        the_dict = self.__dict__.copy()
        the_dict['__class__'] = self.__class__.__name__
        the_dict['created_at'] = self.created_at.isoformat()
        the_dict['updated_at'] = self.updated_at.isoformat()
        return the_dict
