#!/usr/bin/python3
"""
Base Model Module

"""

from datetime import datetime
import uuid

class BaseModel:
    """
    Base Model Class

    """

    def __init__(self) -> None:
        """
        Init Method

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """
        
        """
        return '[{0}] ({1})'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with current datetime

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns dictionary containing all keys/values
        
        """
        class_details = self.__dict__
        class_details['__class__'] = self.__class__.__name__
        class_details['created_at'] = self.created_at.isoformat()
        class_details['updated_at'] = self.updated_at.isoformat()

        return class_details
