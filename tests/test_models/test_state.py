#!/usr/bin/python3
"""Test Module implementation for State """
import unittest
import pep8
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.base_model import BaseModel
from os import getenv, remove


storage = getenv("HBNB_TYPE_STORAGE", "fs")


class test_state(unittest.TestCase):
    """Test cases for Class State """

    @classmethod
    def setUpClass(cls):
        """ Sets up unittest"""
        cls.new_state = State()
        cls.new_state.name = "California"

    @classmethod
    def tearDownClass(cls):
        """ Tears down unittest"""
        del cls.new_state
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_States_dbtable(self):
        """ Check if the tablename is correct"""
        self.assertEqual(self.new_state.__tablename__, "states")

    def test_State_inheritence(self):
        """Test that State class inherits from BaseModel."""
        self.assertIsInstance(self.new_state, BaseModel)

    def test_State_attributes(self):
        """Test that State class contains the attribute `name`."""
        self.assertTrue("name" in self.new_state.__dir__())

        @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_State_attributes_type(self):
        """ Test that State class attribute name is class type str."""
        name = getattr(self.new_state, "name")
        self.assertIsInstance(name, str)
