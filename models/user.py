#!/usr/bin/python3
"""
This module contains the User class (Blueprint for creating user objects).
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This is the user class.

    Attributes:
        email (str)
        password (str)
        first_name (str)
        last_name (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize public instance attributes.
        """
        super().__init__(*args, **kwargs)


