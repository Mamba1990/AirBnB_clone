#!/usr/bin/python3
"""Represents the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a city.

    Attributes:
        state_id (str): The state's id.
        name (str): The city's name.
    """

    state_id = ""
    name = ""
