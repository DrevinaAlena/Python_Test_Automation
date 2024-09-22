import unittest
import math
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """initialization of calculation"""
        self.calc = Calculator()

    def test_sum(self):
        """sum"""
        result = self.calc.add(1, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        """multiplication"""
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_subtract(self):
        """substraction"""
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_divide(self):
        """division"""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_sqrt(self):
        """square root"""
        result = self.calc.sqrt(16)
        self.assertEqual(result, 4)

    def test_pi(self):
        """pi value"""
        pi_value = self.calc.pi()
        self.assertEqual(pi_value, math.pi)


if __name__ == '__main__':
    unittest.main()