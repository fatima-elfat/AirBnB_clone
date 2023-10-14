#!/usr/bin/python3
"""
the unitesst for Amenity.
"""

from models.amenity import Amenity
import unittest
import os
import models
from time import sleep
from datetime import datetime

class TestAmenity(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.my_model = Amenity()
        self.my_model.name = "fridge"

    @classmethod
    def tear(self):
        del self.my_model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()