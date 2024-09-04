import unittest
from BE.calculator_helper import CalculatorHelper

class TestCalculatorHelper(unittest.TestCase):
    def setUp(self):
        self.calculator = CalculatorHelper()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 7), 8)
        self.assertEqual(self.calculator.add(-1, -1), -2)
        self.assertEqual(self.calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 4), 12)
        self.assertEqual(self.calculator.multiply(-1, -1), 1)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-10, -2), 5)
        self.assertEqual(self.calculator.divide(-10, 2), -5)

    def test_divide_by_zero(self):
        result = self.calculator.divide(10, 0)
        self.assertIsNone(result)  # Since the logger is used and the result is None

if __name__ == '__main__':
    unittest.main()
