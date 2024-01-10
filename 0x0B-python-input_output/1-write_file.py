#!/usr/bin/python3
"""Defines a function for filewriting"""


def write_file(filename="", text=""):
    """Write a string text to textfile encoded in UTF8.


    Args:
        filename (str): Name of the file to write.
        text (str): Text to be written in file.
    Returns:
        Number of chars written.
    """
    with open(filename, "w", encoding="utf-8") as myFile:
        return myFile.write(text)
