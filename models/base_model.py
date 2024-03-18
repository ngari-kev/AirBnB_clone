#!/usr/bin/python3
from datetime import datetime
import uuid
"""
    This is a module that contains the base model.
"""


class BaseModel():
    """
    This is a class that other classes inherit from.

    """
    def __init__(self):
        """
        initializes a new instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns formatted string representing the instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the attribute updated_at.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns:
            dictionary containing all keys/values of __dict__ of the instance.
        """
        o_dict = self.__dict__.copy()
        o_dict['__class__'] = self.__class__.__name__
        o_dict['created_at'] = self.created_at.isoformat()
        o_dict['updated_at'] = self.updated_at.isoformat()
        return o_dict