#!/usr/bin/python3
"""Defines a class-instance compare function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class.

    Args:
        obj (any): The object passed as arg to be checked.
        a_class (type): The class to cross-match the type of obj to.
    Returns:
        True - If obj is exactly an instance of a_class.
        False - Otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
