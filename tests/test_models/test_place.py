#!/usr/bin/python3
"""Implementation of Place test models """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.base_model import BaseModel
from os import getenv, remove


storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestPlace(unittest.TestCase):
    """Tests Class Place """

    @classmethod
    def setUpClass(cls):
        """ Sets up unittest"""
        cls.new_place = Place(city_id="0O01", user_id="0O02", name="house",
                              description="awesome", number_rooms=3,
                              number_bathrooms=2, max_guest=1,
                              price_by_night=100, latitude=37.77,
                              longitude=127.12)

        @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittest
        '''
        del cls.new_place
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_Place_dbtable(self):
        """Check if the tablename is correct"""
        self.assertEqual(self.new_place.__tablename__, "places")

    def test_Place_inheritance(self):
        """tests that the City class Inherits from BaseModel"""
        self.assertIsInstance(self.new_place, BaseModel)@unittest.skipIf(storage == "db", "Testing database storage only")
    def test_place_amenity_attrb(self):
        self.assertTrue("amenity_ids" in self.new_place.__dir__())

    @unittest.skipIf(storage != "db", "Testing database storage only")
    def test_place_amenity_dbattrb(self):
        self.assertTrue("amenities" in self.new_place.__dir__())
        self.assertTrue("reviews" in self.new_place.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_longitude(self):
        """Test the type of longitude."""
        longitude = getattr(self.new_place, "longitude")
        self.assertIsInstance(longitude, float)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_latitude(self):
        """Test the type of latitude"""
        latitude = getattr(self.new_place, "latitude")
        self.assertIsInstance(latitude, float)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_price_by_night(self):
        """Test the type of price_by_night"""
        price_by_night = getattr(self.new_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_max_guest(self):
        """Test the type of max_guest"""
        max_guest = getattr(self.new_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_number_bathrooms(self):
        """ Test the type of number_bathrooms"""
        number_bathrooms = getattr(self.new_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_number_rooms(self):
        """ Test the type of number_bathrooms"""
        number_rooms = getattr(self.new_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_description(self):
        """Test the type of description"""
        description = getattr(self.new_place, "description")
        self.assertIsInstance(description, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_name(self):
        """ Test the type of name"""
        name = getattr(self.new_place, "name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_user_id(self):
        """ Test the type of user_id"""
        user_id = getattr(self.new_place, "user_id")
        self.assertIsInstance(user_id, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_city_id(self):
        """ Test the type of city_id"""
        city_id = getattr(self.new_place, "city_id")
        self.assertIsInstance(city_id, str)
