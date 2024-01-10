#!/usr/bin/python3
"""Defination of a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization of a new Student.

        Args:
            first_name (str): The student first name.
            last_name (str): The students last name.
            age (int): The student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student."""
        return self.__dict__
