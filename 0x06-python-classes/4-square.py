#!/usr/bin/python3
"""Defination to a class Square."""


class Square:
    """square representation."""

    def __init__(self, size=0):
        """A new square initialization.
        Argument size : The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get and set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value_size):
        if not isinstance(value_size, int):
            raise TypeError("size must be an integer")
        elif value_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value_size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
