#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Createa an object from JSON file."""
    with open(filename) as myFile:
        return json.load(myFile)
