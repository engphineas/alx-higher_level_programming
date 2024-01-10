#!/usr/bin/python3
"""Defination to a function that adds attributes to objects."""


def add_attribute(obj, attributes, value):
    """Function adds a new attribute to an object.

    Args:
        obj (any): The object to be added an attribute to.
        attributes (str): Name of the attribute to add to the object.
        value (any): The value of attribute.
    Raises:
        TypeError: If not possible to add the attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attributes, value)
