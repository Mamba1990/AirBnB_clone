#!/usr/bin/python3
"""Represents the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Definess the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializing the new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairing for attributes.
        """
        t_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, t_form)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Updating the attribute updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary that contains keys/values 
        of __dict__ of the instance.    
        """
        r_dict = self.__dict__.copy()
        r_dict["created_at"] = self.created_at.isoformat()
        r_dict["updated_at"] = self.updated_at.isoformat()
        r_dict["__class__"] = self.__class__.__name__
        return r_dict

    def __str__(self):
        """Displays the print/str representation of the BaseModel instance."""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
