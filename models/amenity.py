#!/usr/bin/python3
"""
the module of Amenity.
it inherits from BaseModel.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class of Amenity.
    Attributes:
        name (str): amenities name.

    """
    name = ""