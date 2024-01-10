#!/usr/bin/python3
"""Defines Python class-to-JSON function."""


def class_to_json(obj):
    """Returns the dict representation with a simple data structure."""
    return obj.__dict__
