import unittest
import task
import math

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

if __name__ == '__main__':
    unittest.main()