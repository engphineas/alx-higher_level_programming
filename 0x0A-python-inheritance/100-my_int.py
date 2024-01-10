#!/usr/bin/python3
"""Defines a class MyInt inherits from int."""


class MyInt(int):
    """Function inverts int operators == and !=."""

    def __eq__(self, value):
        """Override == operator with != property."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == property."""
        return self.real == value
