#!/usr/bin/python3
"""Represents the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines an amenity.

    Attributes:
        name (str): The amenity's name.
    """

    name = ""
