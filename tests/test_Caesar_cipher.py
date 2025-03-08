from production_code.Caesar_cipher import caesar_cipher
import unittest


class TestCaesarCipher(unittest.TestCase):
    def test_basic_rotation(self):
        s = "abc"
        k = 1
        expected = "bcd"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)

    def test_case_preservation(self):
        s = "AbC"
        k = 2
        expected = "CdE"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)

    def test_large_rotation(self):
        s = "xyz"
        k = 27  
        expected = "yza"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)

    def test_with_hyphen(self):
        s = "middle-outz"
        k = 2
        expected = "okffng-qwvb"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        s = ""
        k = 3
        with self.assertRaises(ValueError):
            caesar_cipher(s, k)
