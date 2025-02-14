import unittest
from classes import AdditonSub


class TestAdditionSubtraction(unittest.TestCase):
    def test_add(self):
        add_sub = AdditonSub()
        self.assertEqual(add_sub.add(5, 5), 10)

    def test_subtract(self):
        add_sub = AdditonSub()
        self.assertEqual(add_sub.subtract(5, 5), 0, "hellow world")
