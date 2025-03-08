from production_code.Funny_string import funny_string
import unittest

class TestFunnyString(unittest.TestCase):
    def test_funny_string_acxz(self):
        s = "acxz"
        expected = "Funny"

        result = funny_string(s)

        self.assertEqual(result, expected)

    def test_not_funny_string_bcxz(self):
        s = "bcxz"
        expected = "Not Funny"

        result = funny_string(s)

        self.assertEqual(result, expected)

    def test_single_char(self):
        s = "a"
        expected = "Funny"

        result = funny_string(s)

        self.assertEqual(result, expected)

    def test_length_out_of_range_low(self):
        s = ""

        with self.assertRaises(ValueError):
            funny_string(s)

    def test_length_out_of_range_high(self):
        s = "a" * 10001

        with self.assertRaises(ValueError):
            funny_string(s)

