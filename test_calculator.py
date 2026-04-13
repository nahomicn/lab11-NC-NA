# https://github.com/nahomicn/lab11-NC-NA
# Partner 1: Nahomi Carrazana
# Partner 2: N/A (No partner assigned)

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(16), 4)

if __name__ == "__main__":
    unittest.main()
