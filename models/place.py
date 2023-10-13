#!/usr/bin/python3
"""Reprents the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a place.

    Attributes:
        city_id (str): The City's id.
        user_id (str): The User's id.
        name (str): The place's name.
        description (str): The place's description
        number_rooms (int): The place's number of rooms.
        number_bathrooms (int): The place's number of bathrooms.
        max_guest (int): The place.'s max number of guests.
        price_by_night (int): The place's price by night.
        latitude (float): The place's latitude.
        longitude (float): The place's longitude.
        amenity_ids (list): The Amenity ids' list
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
