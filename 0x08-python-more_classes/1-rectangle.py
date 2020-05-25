#!/usr/bin/python3
""" Module for rectangle class """


class Rectangle:
    """  Class Rectangle that defines a rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for property width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for property width """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for property heigth """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for property heigth """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
