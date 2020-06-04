#!/usr/bin/python3
"""Student Module"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Initalizates a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list and all(type(i) is str for i in attrs):
            new_dict = {}
            for at in attrs:
                if hasattr(self, at):
                    new_dict[at] = self.__dict__[at]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
