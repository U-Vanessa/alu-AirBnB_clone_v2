#!/usr/bin/python3
"""
This module contains Amenity class (Blueprint for creating Amenity objects).
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This is the amenity class

    Attributes:
        name 
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.name = Amenity.name
