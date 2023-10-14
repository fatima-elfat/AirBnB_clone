#!/usr/bin/python3
"""
the module of State.
it inherits from BaseModel.
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    class States.
    Attributes:
        name (str): statexs name.
    """
    name = ""
