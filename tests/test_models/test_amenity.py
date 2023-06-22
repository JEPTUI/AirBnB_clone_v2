#!/usr/bin/python3
"""Amenity test models implemented """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel
from os import getenv, remove
import pep8


storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity Class"""

    @classmethod
    def setUpClass(cls):
        """ Sets up unittest"""
        cls.new_amenity = Amenity()
        cls.new_amenity.name = "TV"

    @classmethod
    def tearDownClass(cls):
        """ Tears down unittest"""
        del cls.new_amenity
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8_style_check(self):
        """ Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error needs fixing")

    def test_States_dbtable(self):
        """ Checks if the tablename is correct"""
        self.assertEqual(self.new_amenity.__tablename__, "amenities")

    def test_Amenity_inheritence(self):
        """ tests that the Amenity class Inherits from BaseModel"""
        self.assertIsInstance(self.new_amenity, BaseModel)

        @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_Amenity_attribute_type(self):
        """ Test that Amenity class had name attribute's type."""
        name_value = getattr(self.new_amenity, "name")
        self.assertIsInstance(name_value, str)
