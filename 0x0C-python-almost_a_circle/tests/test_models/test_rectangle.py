#!/usr/bin/python3
# test_rectangle.py
"""Defines unittests for models/rectangle.py.
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle



class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for instantiation of the Rectangle class testing."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)
