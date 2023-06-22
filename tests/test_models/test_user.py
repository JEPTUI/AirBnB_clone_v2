#!/usr/bin/python3
"""Test Module implementation for User """
import unittest
import pep8
import sys
import datetime
from models.base_model import BaseModel
from models.user import User
from os import getenv, remove
from io import StringIO


storage = getenv("HBNB_TYPE_STORAGE", "fs")


class test_User(unittest.TestCase):
    """Test cases for class User """

    @classmethod
    def setUpClass(cls):
        """ Sets up unittest"""
        cls.new_user = User()
        cls.new_user.email = "email@gmail.com"
        cls.new_user.password = "password"
        cls.new_user.firt_name = "Mel"
        cls.new_user.last_name = "Ng"

    @classmethod
    def tearDownClass(cls):
        """ Tear down unittest"""
        del cls.new_user
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_User_dbtable(self):
        """Checks if the tablename is correct"""
        self.assertEqual(self.new_user.__tablename__, "users")

    def test_User_inheritance(self):
        """ tests that the User class Inherits from BaseModel"""
        self.assertIsInstance(self.new_user, BaseModel)

    def test_User_attributes(self):
        """ Test the user attributes exist"""
        self.assertTrue("email" in self.new_user.__dir__())
        self.assertTrue("first_name" in self.new_user.__dir__())
        self.assertTrue("last_name" in self.new_user.__dir__())
        self.assertTrue("password" in self.new_user.__dir__())

        @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_email(self):
        """ Test the type of name"""
        name = getattr(self.new_user, "email")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_first_name(self):
        """ Test the type of name"""
        name = getattr(self.new_user, "first_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_last_name(self):
        """ Test the type of last_name"""
        name = getattr(self.new_user, "last_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_password(self):
        """ Test the type of password """
        name = getattr(self.new_user, "password")
        self.assertIsInstance(name, str)
