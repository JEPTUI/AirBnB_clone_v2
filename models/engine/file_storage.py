#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """Implements simple file storage."""

    __file_path = "file.json"
    __objects = {}

    @staticmethod
    def get_constructor(class_name):
        """Return a valid class constructor given a valid class name."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        return classes.get(class_name)

    def all(self):
        """Return dictionary of all stored objects."""
        return self.__objects

    def new(self, obj):
        """Add new obj to __objects with key <obj class name>.id."""
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj_key] = obj

    def save(self):
        """Serialize __objects to JSON file."""
        objects_serialized = {}

        # ensure every object in __objects can be serialized
        for obj_key, obj in self.__objects.items():
            try:
                objects_serialized[obj_key] = obj.to_dict()
            except Exception:
                objects_serialized[obj_key] = obj.__dict__

        # write objects_serialized to file_path
        try:
            with open(self.__file_path, "w") as f_write:
                json.dump(objects_serialized, f_write)
        except Exception:
            raise Exception(f"Error: Could not write to {self.__file_path}")

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            # remove all objects currently in memory
            self.__objects.clear()

            objects_loaded = {}

            # read content of file_path
            try:
                with open(self.__file_path, "r") as f_read:
                    objects_loaded = json.load(f_read)
            except Exception:
                pass

            # deserialize the objects in objects_loaded
            for obj_key, obj_dict in objects_loaded.items():
                class_name = obj_dict.get("__class__")
                constructor = self.get_constructor(class_name)

                if constructor is None:
                    raise Exception(f"Error: Invalid class name: {class_name}")

                self.__objects[obj_key] = constructor(**obj_dict)

        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """method for deserializing the JSON file to objects"""
        self.reload()
