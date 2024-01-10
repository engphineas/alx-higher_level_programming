#!/usr/bin/python3
"""Unittests for list max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test to an ordered list of integers."""
        ordered = [2, 4, 6, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered_list(self):
        """Test to an unordered list of integers."""
        unordered = [8, 2, 4, 6]
        self.assertEqual(max_integer(unordered), 8)

    def test_max_at_begginning(self):
        """Test a list with max value at the beginning."""
        max_at_beginning = [8, 6, 4, 2]
        self.assertEqual(max_integer(max_at_beginning), 8)

    def test_empty_list(self):
        """Test to an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a single element list."""
        one_element = [5]
        self.assertEqual(max_integer(one_element), 5)

    def test_floats(self):
        """Test a list of floats."""
        floats = [8.12, 5.333, -9.3, 5.5, 8.30]
        self.assertEqual(max_integer(floats), 8.30)

    def test_ints_and_floats(self):
        """Test a list of combined ints and floats."""
        ints_and_floats = [23, 8.12, -9.3, 8.3, 6]
        self.assertEqual(max_integer(ints_and_floats), 23)

    def test_string(self):
        """Test to a string."""
        string = "Python"
        self.assertEqual(max_integer(string), 'y')

    def test_list_of_strings(self):
        """Test to a list of strings."""
        strings = ["Python", "is", "fun"]
        self.assertEqual(max_integer(strings), "Python")

    def test_empty_string(self):
        """Test to an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
