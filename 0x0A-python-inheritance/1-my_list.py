#!/usr/bin/python3
"""Defines an inherited list class called MyList."""


class MyList(list):
    """Prints sorted list for the built-in list class."""

    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))
