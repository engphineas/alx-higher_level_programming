#!/usr/bin/python3

"""defines Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Representation of a Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of a new Rectangle.

        Args:
            width (int): Width of new Rectangle.
            height (int): Height of new Rectangle.
            x (int): x value of new Rectangle.
            y (int): y value of new Rectangle.
            id (int): Id of new Rectangle.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height <= 0.
            TypeError: If x or y is not an integer.
            ValueError: If x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter to the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter to the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter to the x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter to the y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Returns the area of Rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle using #."""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for h in range(self.y)]
        for p in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for z in range(self.width)]
            print("")

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y,
                self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the Rectangle.Assign arguments to attributes in position.

        Args:
            *args (ints): New attribute values.
                1st argument reps id attribute
                2nd argument reps width attribute
                3rd argument reps height attribute
                4th argument reps x attribute
                5th argument reps y attribute
            **kwargs (dict): New key and value pairs of attributes.
        """
        if args:
            for attributes, arg in enumerate(args):
                if attributes == 0:
                    self.id = arg
                elif attributes == 1:
                    self.width = arg
                elif attributes == 2:
                    self.height = arg
                elif attributes == 3:
                    self.x = arg
                elif attributes == 4:
                    self.y = arg
                else:
                    continue

        elif len(kwargs) > 0:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val
                else:
                    break

    def to_dictionary(self):
        """Returns a dict rep of a Rectangle."""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
