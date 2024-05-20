#!/usr/bin/python3
"""
This module contains the City class (Blueprint for creating City objects).
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    This is the city class

    Attributes:
        state_id 
        name 
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.name = City.name
        # self.state_id = City.state_id
