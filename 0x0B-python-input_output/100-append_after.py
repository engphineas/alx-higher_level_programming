#!/usr/bin/python3
"""Defination of a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """function inserts text after each line of a given string in a file.

    Args:
        filename (str): The name of file.
        search_string (str): The string to search from within the file.
        new_string (str): The string to be inserted.
    """
    new_text = ""
    with open(filename) as myFile:
        for line in myFile:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, "w") as file_new:
        file_new.write(new_text)
