from unittest import TestCase
from Triangle import Node


class TestNode(TestCase):
    def test_init(self):
        try:
            Node(5, 7)
        except AssertionError:
            self.fail()

        with self.assertRaises(AssertionError):
            Node(8, 3)

    def test_get_abs_idx(self):
        to_check = [(0, (0, 0)),
                    (1, (0, 1)),
                    (4, (1, 2)),
                    (8, (2, 3))]
        for expected, pos in to_check:
            self.assertEqual(expected, Node(*pos).get_abs_idx())
