import unittest
from calculator import divide_numbers

class TestDivision(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(divide_numbers(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide_numbers(-10, -2), 5)

    def test_divide_by_one(self):
        self.assertEqual(divide_numbers(10, 1), 10)

    def test_division_by_zero(self):
        self.assertEqual(divide_numbers(10, 0), "Error: Cannot divide by zero.")

    def test_divide_zero_by_number(self):
        self.assertEqual(divide_numbers(0, 10), 0)

    def test_divide_with_floats(self):
        self.assertAlmostEqual(divide_numbers(9.0, 2), 4.5) 

if __name__ == '__main__':
    unittest.main()
