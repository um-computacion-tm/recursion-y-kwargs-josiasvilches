import unittest
from main import factoriales


class TestFactorial(unittest.TestCase):
    def test_factoriales_5(self):
        self.assertEqual(factoriales(5), 120)
    def test_factoriales_2(self):
        self.assertEqual(factoriales(2), 2)
    def test_factoriales_0(self):
        self.assertEqual(factoriales(0), 1)
    def test_factoriales_1(self):
        self.assertEqual(factoriales(1), 1)
    def test_factoriales_10(self):
        self.assertEqual(factoriales(10), 3628800)
    def test_factoriales_20(self):
        self.assertEqual(factoriales(20), 2432902008176640000)
    def test_factoriales_30(self):
        self.assertEqual(factoriales(30), 265252859812191058636308480000000)

unittest.main()