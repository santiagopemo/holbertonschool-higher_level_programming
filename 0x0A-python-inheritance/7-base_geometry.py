#!/usr/bin/python3
"""Base Geometry Module"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Public instance method area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
