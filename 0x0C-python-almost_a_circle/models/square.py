#!/usr/bin/python3
"""Defines a Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square."""


    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of a new Square.


        Args:
            size (int): Size of the Square.
            x (int): x value of the new square.
            y (int): y value of the new square.
            id (int): id of the new square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation."""
        return "[Square]({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter to the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates to the Square.

        Args:
            *args (ints): New square attributes values.
                args0 rep id
                args1 rep size
                args2 rep x
                args3 rep y
            **kwargs (dict): New key and value pairs of the attributes.
        """
        if args:
            for pos, attr_val in enumerate(args):
                if pos == 0:
                    if args is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = attr_val
                elif pos == 1:
                    self.width = attr_val
                elif pos == 2:
                    self.height = attr_val
                elif pos == 3:
                    self.x = attr_val
                elif pos == 4:
                    self.y = attr_val
                else:
                    continue
        elif len(kwargs)> 0:
            for key, attr_val in kwargs.items():
                if key == "id":
                    if attr_val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = attr_val
                elif key == "width":
                    self.width = attr_val
                elif key == "height":
                    self.height = attr_val
                elif key == "x":
                    self.x = attr_val
                elif key == "y":
                    self.y = attr_val
                else:
                    break

    def to_dictionary(self):
        """Returns the dict representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

