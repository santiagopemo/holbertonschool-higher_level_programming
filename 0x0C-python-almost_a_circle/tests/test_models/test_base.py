#!/usr/bin/python3
"""Test Base Module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    """TestBase Class"""
    def setUp(self):
        pass

    def tearDown(self):
        Base._Base__nb_objects = 0
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.isfile("Square.json"):
            os.remove("Square.json")
        if os.path.isfile("Base.json"):
            os.remove("Base.json")

    def test_single_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_zero_id(self):
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_multiples_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_set_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_two_instances(self):
        b1 = Base()
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_two_instances2(self):
        b1 = Base(98)
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_two_instances3(self):
        b1 = Base()
        b1 = Base(98)
        self.assertEqual(b1.id, 98)

    def test_two_instances4(self):
        b1 = Base(1)
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_nb_objects_private(self):
        self.assertEqual(hasattr(Base, "_Base__nb_objects"), True)
        self.assertEqual(hasattr(Base, "__nb_objects"), False)
        self.assertEqual(hasattr(Base, "nb_objects"), False)
        self.assertEqual(getattr(Base, "__nb_objects", False), False)
        with self.assertRaises(AttributeError):
            a = Base.__nb_objects
        with self.assertRaises(AttributeError):
            a = Base.nb_objects

    def test_nb_objects_value(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(Base._Base__nb_objects, 3)
        self.assertEqual(getattr(Base, "_Base__nb_objects", 0), 3)
        self.assertEqual(Base.__dict__["_Base__nb_objects"], 3)

    def set_nb_objects(self):
        setattr(Base, "_Base__nb_objects", 3)
        b1 = Base()
        self.assertEqual(b1.id, 4)
        Base._Base__nb_objects = 3
        b2 = Base()
        self.assertEqual(b2.id, 4)
        Base.__dict__["_Base__nb_objects"] = 3
        b3 = Base()
        self.assertEqual(b3.id, 4)

    def test_to_json_string_simple(self):
        l_json_string = Base.to_json_string([{"a": 1}])
        self.assertEqual(l_json_string, '[{"a": 1}]')

    def test_to_json_string(self):
        l_dict = []
        l_dict.append({'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        l_dict.append({'x': 2, 'width': 12, 'id': 2, 'height': 10, 'y': 8})
        l_json_string = Base.to_json_string(l_dict)
        l_dict_from_json = json.loads(l_json_string)
        self.assertEqual(type(l_dict_from_json), list)
        self.assertEqual(l_dict_from_json, l_dict)

    def test_to_json_string_two_times(self):
        l_dict = []
        l_dict.append({'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        l_dict.append({'x': 2, 'width': 12, 'id': 2, 'height': 10, 'y': 8})
        l_json_string1 = Base.to_json_string(l_dict)
        l_json_string2 = Base.to_json_string(l_dict)
        self.assertEqual(l_json_string1, l_json_string2)

    def test_to_json_string_type(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_to_json_string_empty(self):
        l_json_string = Base.to_json_string([])
        self.assertEqual(type(l_json_string), str)
        self.assertEqual(l_json_string, "[]")

    def test_to_json_string_None(self):
        l_json_string = Base.to_json_string(None)
        self.assertEqual(type(l_json_string), str)
        self.assertEqual(l_json_string, "[]")

    def test_to_json_string_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(10, 7, 2)
        d1 = r1.to_dictionary()
        d2 = r2.to_dictionary()
        json_string = Base.to_json_string([d1, d2])
        rectangles = json.loads(json_string)
        self.assertDictEqual(d1, rectangles[0])
        self.assertDictEqual(d2, rectangles[1])

    def test_to_json_string_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(10)
        d1 = s1.to_dictionary()
        d2 = s2.to_dictionary()
        json_string = Base.to_json_string([d1, d2])
        squares = json.loads(json_string)
        self.assertDictEqual(d1, squares[0])
        self.assertDictEqual(d2, squares[1])

    def test_to_json_string_zero_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as f:
            json_dict = json.load(f)
        d1 = r1.to_dictionary()
        d2 = r2.to_dictionary()
        self.assertEqual([d1, d2], json_dict)

    def test_save_to_file_squares(self):
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        with open("Square.json") as f:
            json_dict = json.load(f)
        d1 = r1.to_dictionary()
        d2 = r2.to_dictionary()
        self.assertEqual([d1, d2], json_dict)

    def test_save_to_file_exist(self):
        Rectangle.save_to_file([Rectangle(2, 3)])
        Square.save_to_file([Square(2)])
        self.assertEqual(os.path.isfile("Rectangle.json"), True)
        self.assertEqual(os.path.isfile("Square.json"), True)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_zero_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Square.save_to_file()
        
    def test_save_to_file_zero_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])
        with self.assertRaises(TypeError):
            Square.save_to_file([], [])

if __name__ == "__main__":
    unittest.main()
