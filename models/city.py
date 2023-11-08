#!/usr/bin/python3
"""import modules"""
from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.state.id = ""
        self.name = ""
