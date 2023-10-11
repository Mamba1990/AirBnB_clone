#!/usr/bin/python3
"""Represents the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a review.

    Attributes:
        place_id (str): The id of the place.
        user_id (str): The id of the user.
        text (str): The review's text.
    """

    place_id = ""
    user_id = ""
    text = ""
