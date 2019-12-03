# Created by Eddie Garcia at 11/30/19

# Tests for edit distance.

import unittest
import math

from Python.Lab7.main import get_left_top_corner
from Python.Lab7.main import build_2d_array
from Python.Lab7.main import check_values
from Python.Lab7.main import edit_distance


class TestLab7(unittest.TestCase):
    def setUp(self) -> None:
        self.s1 = "eddie"
        self.s2 = "eddie"


class TestEditDistance(TestLab7):
    def test_build_2d_array(self):
        x_size = 4
        y_size = 4

        expected_list = [
            [0, 1, 2, 3],
            [1, math.inf, math.inf, math.inf],
            [2, math.inf, math.inf, math.inf],
            [3, math.inf, math.inf, math.inf]
        ]
        self.assertEqual(expected_list, build_2d_array(y_size, x_size))

    def test_get_top_left_corner(self):
        # Function tested at test case 'test_build_2d_array'.
        ints = build_2d_array(2, 2)
        left, top, corner = get_left_top_corner(ints, 0, 1)
        self.assertEqual(1, corner)
        self.assertEqual(0, top)
        self.assertEqual(math.inf, left)
        self.assertEqual(0, min(left, top, corner))

    def test_check_values(self):
        self.assertEqual(False, check_values(self.s1, self.s2))
        self.assertEqual(True, check_values(self.s1, None))
        self.assertEqual(True, check_values(1, 1))

    def test_edit_distance_none_values_ints(self):
        self.assertEqual(None, edit_distance(None, None))
        self.assertEqual(None, edit_distance(1, 2))
        self.assertEqual(None, edit_distance(None, 2))
        self.assertEqual(None, edit_distance(1, None))

    def test_edit_distance_s(self):
        expected_list = [
            [0, 1, 2, 3, 4, 5],
            [1, 0, 1, 2, 3, 4],
            [2, 1, 0, 1, 2, 3],
            [3, 2, 1, 0, 1, 2],
            [4, 3, 2, 1, 0, 1],
            [5, 4, 3, 2, 1, 0]
        ]
        expected_distance = 0
        values = edit_distance(self.s1, self.s2)

        self.assertEqual(expected_distance, values[0])
        self.assertEqual(expected_list, values[1])
