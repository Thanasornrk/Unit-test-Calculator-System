import unittest
import calculator #Import the file we want to test

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator.add(3,5),8)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(calculator.sub(10, 4), 6)
        self.assertEqual(calculator.sub(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 7), 21)
        self.assertEqual(calculator.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(9, 3), 3)
        self.assertEqual(calculator.divide(5, 0), "Cannot divide by zero")  # test division by zero

if __name__ == '__main__':
    unittest.main()