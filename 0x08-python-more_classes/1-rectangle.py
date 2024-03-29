#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """
    This class defines a rectangle by: (based on 1-rectangle.py)
    Attributes:
        width: this is the width of the rectangle
        height: this is the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """This initializes the instance and assigns attributes
        Args:
            width: this is the width of the rectangle
            height: this is the height of the rectangle
        Return: this returns the height and width of a rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Gets the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """value: sets the width value
        """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """value: sets the height value
        """
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
