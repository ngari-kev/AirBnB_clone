#!/usr/bin python3

from models.base_model import BaseModel
"""
This module contains the User class.
"""


class User(BaseModel):
    """
    Defines a class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
