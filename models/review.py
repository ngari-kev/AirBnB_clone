#!/usr/bin/python3

"""
Contains the review class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines the Review class. Inherits from BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""
