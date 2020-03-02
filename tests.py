import unittest
import task
import math
import datetime


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())


class CircleCase(unittest.TestCase):
    def test1(self):
        expected = math.pi * 16
        self.assertEqual(expected, task.circlerun(4))


class ListCase(unittest.TestCase):
    def test1(self):
        expected = [1, 4]
        self.assertEqual(expected, task.listrun([1, 2, 3, 4]))

class DateCase(unittest.TestCase):
    def test1(self):
        date1 = datetime.date(2020, 5, 19)
        date2 = datetime.date(2022, 5, 19)
        expected = 730
        self.assertEqual(expected, task.daterun(date1, date2))


if __name__ == '__main__':
    unittest.main()
