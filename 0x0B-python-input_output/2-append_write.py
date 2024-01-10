#!/usr/bin/python3
""" Defines a function to do file-appending."""


def append_write(filename="", text=""):
    """Appends a string at the end of UTF8 text file.


    Args:
        filename (str): Name of the file to be appended text.
        text (str): String to be appended into the file.
    Returns:
        Number of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)
