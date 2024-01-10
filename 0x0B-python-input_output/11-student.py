#!/usr/bin/python3
"""Defination of a class Student."""


class Student:
    """Representation of a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization a new Student.

        Args:
            first_name (str): The students first name.
            last_name (str): The students last name.
            age (int): The student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of the Student.

        If attrs is a list of strings, that represents only those attributes
        included in the list.

        Args:
            attrs (list): Attributes to represent (optional and can be null.
        """
        if (type(attrs) == list and
                all(type(elements) == str for elements in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student.

        Args:
            json (dict): The key and value pairs to replace attributes with.
        """
        for j, k in json.items():
            setattr(self, j, k)
