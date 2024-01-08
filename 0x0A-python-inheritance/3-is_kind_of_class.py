#!/usr/bin/python3
"""Defines a class and inherited class-instance checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of or inherited instance of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to cross-match the type of obj to.
    Returns:
        True - if obj is an instance or inherited instance of a_class.
        False - If otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
