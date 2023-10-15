#!/usr/bin/python3
"""
the module of User.
Inherits from BaseModel.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Represent a User.
    Attributes:
        email (str): email.
        password (str): password.
        first_name (str): first name.
        last_name (str): last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User"""
        super().__init__(*args, **kwargs)