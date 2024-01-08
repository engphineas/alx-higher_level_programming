#!/usr/bin/python3
"""Defines an object attributes and method lookup function."""


def lookup(obj):
    """Returns a list of an object's attributes and methods available."""
    return (dir(obj))
