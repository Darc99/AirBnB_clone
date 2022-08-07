#!/usr/bin/python3
"""
Base Model Module

"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """
    Base Model Class

    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Init Method

        """
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """
        
        """
        return '[{0}] ({1}) {2}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with current datetime

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary containing all keys/values
        
        """
        class_details = self.__dict__.copy()
        class_details['__class__'] = self.__class__.__name__
        class_details['created_at'] = self.created_at.isoformat()
        class_details['updated_at'] = self.updated_at.isoformat()

        return class_details
