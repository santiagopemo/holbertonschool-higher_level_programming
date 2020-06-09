#!/usr/bin/python3
"""Base Module"""
import json
import csv
from os import path


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializtes a Base class instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = []
                for obj in list_objs:
                    dict_list.append(obj.to_dictionary())
                f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode="r") as f:
                dict_list = Base.from_json_string(f.read())
                obj_list = []
                for dic in dict_list:
                    obj_list.append(cls.create(**dic))
                return obj_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV format"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for o in list_objs:
                    values = [o.id, o.width, o.height, o.x, o.y]
                    writer.writerow(values)
            if cls.__name__ == "Square":
                for o in list_objs:
                    values = [o.id, o.size, o.x, o.y]
                    writer.writerow(values)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV format"""
        filename = "{}.csv".format(cls.__name__)
        if not path.isfile(filename):
            return []
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            if cls.__name__ == "Rectangle":
                rect_list = []
                for row in reader:
                    r_dict = {}
                    r_dict["id"] = int(row[0])
                    r_dict["width"] = int(row[1])
                    r_dict["height"] = int(row[2])
                    r_dict["x"] = int(row[3])
                    r_dict["y"] = int(row[4])
                    rect_list.append(cls.create(**r_dict))
                return rect_list
            if cls.__name__ == "Square":
                sq_list = []
                for row in reader:
                    s_dict = {}
                    s_dict["id"] = int(row[0])
                    s_dict["size"] = int(row[1])
                    s_dict["x"] = int(row[2])
                    s_dict["y"] = int(row[3])
                    sq_list.append(cls.create(**s_dict))
                return sq_list
