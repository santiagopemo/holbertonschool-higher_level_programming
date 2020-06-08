#!/usr/bin/python3
"""Test Rectangle Module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json
import os


class TestRectangle(unittest.TestCase):
    """TestRectangle Class"""
    def setUp(self):
        pass

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_empty_instance(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_one_arg_instance(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_six_args_instance(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, 1, 1, 1)

    def test_is_subclass(self):
        self.assertEqual(issubclass(Rectangle, Base), True)

    def is_instance(self):
        self.assertEqual(isinstance(Rectangle, Base), True)

    def test_id(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r4.id, 14)

    def test_id_none(self):
        r4 = Rectangle(3, 5, 6, 7, None)
        self.assertEqual(r4.id, 1)

    def test_width(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r3.width, 6)
        self.assertEqual(r4.width, 3)

    def test_height(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r4.height, 5)

    def test_x(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.x, 2)
        self.assertEqual(r4.x, 6)

    def test_x(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 3)
        r3 = Rectangle(6, 4, 2, 2)
        r4 = Rectangle(3, 5, 6, 7, 14)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.y, 2)
        self.assertEqual(r4.y, 7)

    def test_width_private(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(hasattr(r1, "__width"), False)
        self.assertEqual(hasattr(r1, "_Rectangle__width"), True)

    def test_height_private(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(hasattr(r1, "__height"), False)
        self.assertEqual(hasattr(r1, "_Rectangle__height"), True)

    def test_x_private(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(hasattr(r1, "__x"), False)
        self.assertEqual(hasattr(r1, "_Rectangle__x"), True)

    def test_y_private(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(hasattr(r1, "__y"), False)
        self.assertEqual(hasattr(r1, "_Rectangle__y"), True)

    def test_width_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("four", 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.6, 3)

    def test_height_type(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "four")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, False)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 5.6)

    def test_x_type(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, "four")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, 5.6)

    def test_y_type(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 6, "four")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 6, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 6, 5.6)

    def test_setters(self):
        r4 = Rectangle(3, 5, 6, 7, 14)
        r4.width = 5
        self.assertEqual(r4.width, 5)
        r4.height = 8
        self.assertEqual(r4.height, 8)
        r4.x = 3
        self.assertEqual(r4.x, 3)
        r4.y = 1
        self.assertEqual(r4.y, 1)
        r4.id = 2
        self.assertEqual(r4.id, 2)

    def test_getters(self):
        r4 = Rectangle(5, 8, 3, 1, 2)
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 8)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 1)
        self.assertEqual(r4.id, 2)
    

if __name__ == "__main__":
    unittest.main()
