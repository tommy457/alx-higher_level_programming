#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer([..])."""
    def test_list_ordered(self):
        """Ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_unordered(self):
        """Unordered list of integers."""
        self.assertEqual(max_integer([100, -500, 1, 10]), 100)

    def test_empty_list(self):
        """Empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """List with one element."""
        self.assertEqual(max_integer([98]), 98)

    def test_ints_and_floats_ande(self):
        """List of ints and floats."""
        self.assertEqual(max_integer([3.14, 9.8, -451, 32]), 32)

    def test_string(self):
        """String"""
        self.assertEqual(max_integer("Python"), 'y')

    def test_list_of_strings(self):
        """List of strings."""
        self.assertEqual(max_integer(["C", "is", "Fun"]), "is")

    def test_empty_string(self):
        """Empty string."""
        self.assertEqual(max_integer(""), None)

    def test_string_of_numbers(self):
        """String of numbers"""
        self.assertEqual(max_integer("01932347"), "9")

    def test_inf(self):
        """Inf """
        self.assertEqual(
                max_integer([3.14, float('inf'), float('-inf')]), float('inf'))


if __name__ == '__main__':
    unittest.main()
