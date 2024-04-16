import unittest
from main import fibonacci
class TestFibonacci(unittest.TestCase):
    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(5), 5)
    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1)
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)
    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), 55)
    def test_fibonacci_20(self):
        self.assertEqual(fibonacci(20), 6765)
    def test_fibonacci_30(self):
        self.assertEqual(fibonacci(30), 832040)

unittest.main()