#!/usr/bin/python3
"""Check the behavior of max_integer for representative integer lists."""
import unittest


max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Exercise empty lists, maximum positions, ties, and negative values."""

    def test_empty(self):
        """Return None for an empty list and for the default argument."""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_single(self):
        """Return the only element of a one-element list."""
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-7]), -7)

    def test_maximum_positions(self):
        """Find the maximum at the beginning, middle, or end of a list."""
        for values in ([9, 0, 3], [3, 9, 0], [0, 3, 9]):
            with self.subTest(values=values):
                self.assertEqual(max_integer(values), 9)

    def test_negative_and_duplicate_values(self):
        """Find the maximum among negative values and repeated maxima."""
        self.assertEqual(max_integer([-8, -2, -4]), -2)
        self.assertEqual(max_integer([3, 3, 1, 3]), 3)

    def test_does_not_mutate_input(self):
        """Preserve the input list and its original ordering."""
        values = [5, 1, 8, 2]
        self.assertEqual(max_integer(values), 8)
        self.assertEqual(values, [5, 1, 8, 2])


if __name__ == "__main__":
    unittest.main()
