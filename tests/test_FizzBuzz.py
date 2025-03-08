from production_code.FizzBuzz import fizzbuzz
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_divisible_by_3_shold_return_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_divisible_by_5_shold_return_Buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_divisible_by_3_and_5_shold_return_FizzBuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def test_not_divisible_by_3_or_5_shold_return_not_FizzBuzz(self):
        self.assertEqual(fizzbuzz(7), "not FizzBuzz")
        self.assertEqual(fizzbuzz(11), "not FizzBuzz")

    def test_zero_shold_return_FizzBuzz(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()