#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON-to object function."""
import json


def from_json_string(my_string):
    """Return the Object rep of a JSON string."""
    return json.loads(my_string)
