#!/usr/bin/python3
"""Define a class Student."""


class Student:
    """Representation of a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization of a new Student.

        Args:
            first_name (str): The students first name.
            last_name (str): The students last name.
            age (int): The students age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student.

        If attrs are a list of strings, that represents only those attributes
        in the list.

        Args:
            attrs (list):attributes to represent (Optional and can be empty)
        """
        if (type(attrs) == list and
                all(type(elements) == str for elements in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
