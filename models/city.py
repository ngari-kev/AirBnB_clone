#!/usr/bin/python3

"""Contains the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    defines the city class inheritting from BaseModel
    """
    state_id = ""
    name = ""
