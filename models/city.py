#!/usr/bin/python3
"""
the module of City.
it inherits from BaseModel.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City
    Attributes:
        state_id (str) : the id of the State.
        name (str) : name of the city.
    """
    state_id = ""
    name = ""