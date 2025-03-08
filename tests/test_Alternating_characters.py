from production_code.Alternating_characters import alternating_characters
import unittest

class TestAlternatingCharacters(unittest.TestCase):
    def test_all_same_chars(self):
        s = "AAAA"
        expected = 3

        result = alternating_characters(s)

        self.assertEqual(result, expected)

    def test_already_alternating(self):
        s = "ABABABAB"
        expected = 0

        result = alternating_characters(s)

        self.assertEqual(result, expected)

    def test_mixed_repetitions(self):
        s = "AABABBAA"
        expected = 3

        result = alternating_characters(s)

        self.assertEqual(result, expected)

    def test_length_out_of_range_low(self):
        s = ""

        with self.assertRaises(ValueError):
            alternating_characters(s)

    def test_invalid_characters(self):
        s = "AACB"

        with self.assertRaises(ValueError):
            alternating_characters(s)