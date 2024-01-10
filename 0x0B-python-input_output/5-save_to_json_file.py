#!/usr/bin/python3
"""Defines a JSON file writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object using JSON representation to a text file."""
    with open(filename, "w") as myFile:
        json.dump(my_obj, myFile)
