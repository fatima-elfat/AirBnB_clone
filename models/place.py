#!/usr/bin/python3
"""
the module of Place.
it inherits from BaseModel.
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class of Plase.
    Attributes:
        city_id (str): the id of the City.
        user_id (str): the id of the User.
        description (str): a description od the place.
        number_rooms (int): the number of the rooms.
        number_bathrooms (int): the number of bathrooms.
        max_guest (int): the max number of guests.
        price_by_night (int): the price per night.
        latitude (float): the latitude.
        longitude (float): the longitude.
        amenity_ids (list): A list of all the amenities by id.

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
