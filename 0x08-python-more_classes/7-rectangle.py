#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Representation of a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): Symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of a new Rectangle.

        Args:
            width (int): The new rectangle width.
            height (int): The new rectangle height.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter to the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter to the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns the printable representation of the Rectangle.

        Represent the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle_array = []
        for j in range(self.__height):
            [rectangle_array.append(str(self.print_symbol)) for k in range(self.__width)]
            if j != self.__height - 1:
                rectangle_array.append("\n")
        return ("".join(rectangle_array))

    def __repr__(self):
        """Returns the string representation of the Rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Print a message to every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
