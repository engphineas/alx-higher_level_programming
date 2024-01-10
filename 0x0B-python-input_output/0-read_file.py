#!/usr/bin/python3
"""Defines a function to text file reading."""


def read_file(filename=""):
    """Printing the content of UTF8-encoded text file in the stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
