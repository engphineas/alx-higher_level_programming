#!/usr/bin/python3

"""Defines base class."""
import json
import csv


class Base:
    """Represents Base Model.
    used as "base" for all other classes in the project.
    
    Attributes to Private Class:
        __nb_object (int): rep number of instantiated bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a new Base.

        Args:
            id (int): The identity to the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON serialization of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dicts.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON serialization rep a list of objects to a file.

        Args:
            list_objs (list): The list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                json_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the deserialization of a JSON string.

        Args:
            json_string (str): JSON string representation of a list of dicts.
        Returns:
            If json_string is empty or None - an empty list.
            Otherwise - Python list is represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Returns a class instantied from a dictionary of attrbs.

        Args:
            **dictionary (dict): Key and value pairs of attrbs to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_dummy = cls(1, 1)
            else:
                new_dummy = cls(1)
            new_dummy.update(**dictionary)
            return new_dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes instantiated from a file of JSON-strings.

        Reading from `<cls.__name__>.json`.

        Returns:
            Empty list- If the file does not exist.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as json_file:
                list_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**k) for k in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV of a list of objects to a file.

        Args:
            list_objs (list): list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for objct in list_objs:
                    writer.writerow(objct.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes from a CSV file.

        Reading from file `<cls.__name__>.csv`.

        Returns:
            An empty list - If the file does not exist.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_file, fieldnames=fieldnames)
                list_dicts = [dict([j, int(w)] for j, w in k.items())
                              for k in list_dicts]
                return [cls.create(**k) for k in list_dicts]
        except FileNotFoundError:
            return []
