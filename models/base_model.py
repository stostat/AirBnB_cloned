#!/usr/bin/python3
"""Module for BaseClass for HBnB."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Define all common attributes/methods that other classes can inherit
    Attributes:
        created_at (datetime): Current datetime when an instance is created.
        id (str): Assign an uuid when an instance is created.
        updated_at (datetime): Current datetime when an instance is updated.
    """

    def __init__(self, *args, **kwargs):
        """Initiliaze new instance of BaseModel.
        Args:
            *args: Not used - Arguments list.
            **kwargs: Dictionary of arguments.
        """
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f'))
                elif not key == "__class__":
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Represent a instance as string.
        Returns:
            str: Class name, id, dictionary.
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary containing all keys/values of __dict__.
        Returns:
            dict: All keys/values of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
