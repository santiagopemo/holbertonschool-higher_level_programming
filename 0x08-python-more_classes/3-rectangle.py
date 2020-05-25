#!/usr/bin/python3
""" Module for rectangle class """


class Rectangle:
    """  Class Rectangle that defines a rectangle """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter for property width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for property width """
        if type(value) is not int:
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

    def area(self):
        """ Method that returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ Method that returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Method that return a string with  the
        rectangle represented with the character #
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            for h in range(self.__height):
                string += self.__width * "#" + "\n"
            string = string[:-1]
        return string
