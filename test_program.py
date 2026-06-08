import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../konsolowa')))
from program import caesar_cipher

class TestCaesarCipher(unittest.TestCase):

    def test_basic_data_positive_key(self):
        """Test 1: Dane podstawowe (klucz dodatni, wartość mniejsza od długości alfabetu)"""
        input_text = "abc"
        key = 3
        expected = "def"
        self.assertEqual(caesar_cipher(input_text, key), expected)

    def test_wrapping_out_of_alphabet(self):
        """Test 2: „Zawijanie” (gdy litery w tekście i klucz wychodzą poza alfabet)"""
        input_text = "xyz"
        key = 3
        expected = "abc"
        self.assertEqual(caesar_cipher(input_text, key), expected)

    def test_decryption_negative_key(self):
        """Test 3: Odszyfrowanie (klucz ujemny)"""
        input_text = "def"
        key = -3
        expected = "abc"
        self.assertEqual(caesar_cipher(input_text, key), expected)

    def test_key_greater_than_alphabet_length(self):
        """Test 4: Klucz większy niż długość alfabetu"""
        input_text = "abc"
        key = 29
        expected = "def"
        self.assertEqual(caesar_cipher(input_text, key), expected)

    def test_space_in_text(self):
        """Test 5: Spacja w tekście"""
        input_text = "ab cd"
        key = 2
        expected = "cd ef"
        self.assertEqual(caesar_cipher(input_text, key), expected)

if __name__ == '__main__':
    unittest.main()