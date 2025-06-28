import unittest
from utils import calculate_discount

class DiscountTest(unittest.TestCase):

    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(100, 10), 90)
        self.assertEqual(calculate_discount(200, 50), 100)

    def test_calculate_discount_invalid(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, -10)
        with self.assertRaises(ValueError):
            calculate_discount(100, 110)

if __name__ == '__main__':
    unittest.main()