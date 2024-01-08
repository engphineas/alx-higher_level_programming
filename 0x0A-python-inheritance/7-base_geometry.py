#!/usr/bin/python3
"""Defines a base geometry class namely BaseGeometry."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Not implemented by now."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as int value.

        Args:
            name (str): The parameter name.
            value (int): Parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
