#!/usr/bin/python3
"""defines user module"""

from models.base_model import BaseModel


class User(BaseModel):
    """defines User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
