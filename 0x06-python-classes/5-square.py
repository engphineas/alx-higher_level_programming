#!/usr/bin/python3
"""class Square defination."""


class Square:
    """A square representation."""

    def __init__(self, size):
        """A new square initialization.
        Argument size : size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get and set of the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value_size):
        if not isinstance(value_size, int):
            raise TypeError("size must be an integer")
        elif value_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value_size

    def area(self):
        """Return value is the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for j in range(0, self.__size):
            [print("#", end="") for k in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
