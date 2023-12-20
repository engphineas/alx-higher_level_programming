#!/usr/bin/python3
"""class Square defination."""


class Square:
    """square representation."""

    def __init__(self, size=0):
        """Initialization to a new square.
        Arguments size: The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return current area of the square."""
        return (self.__size * self.__size)
