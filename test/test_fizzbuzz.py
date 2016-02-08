import unittest
from fizzbuzz.fizzbuzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def tearDown(self):
        pass

    def test_fizzbuzz_value_3_returns_fizz(self):
        self.assertEqual(self.fizzbuzz.value(3), 'fizz')

    def test_fizzbuzz_value_5_returns_buzz(self):
        self.assertEqual(self.fizzbuzz.value(5), 'buzz')

    def test_fizzbuzz_value_15_returns_fizzbuzz(self):
        self.assertEqual(self.fizzbuzz.value(15), 'fizzbuzz')

    def test_fizzbuzz_value_7_returns_buzz(self):
        self.assertEqual(self.fizzbuzz.value(7), 7)
