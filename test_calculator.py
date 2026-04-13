# https://github.com/nahomicn/lab11-NC-NA
# Partner 1: Nahomi Carrazana
# Partner 2: N/A (No partner assigned)

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(5, 20), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -5)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2.0)
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)

    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(-2, 3), -6)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(3, 5), -2)


if __name__ == "__main__":
    unittest.main()
