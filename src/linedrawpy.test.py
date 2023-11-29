#!/usr/bin/python3
import unittest
from linedrawpy import is_hex_colour_str_valid

class TestColourValidation(unittest.TestCase):
    """
    linedrawpy should validate background colours
    specified as command line arguments.  Here we
    check validation works correctly.
    """
    def test_valid_colours_accepted(self):
        self.assertTrue(is_hex_colour_str_valid("ffffff") == 1) 
        self.assertTrue(is_hex_colour_str_valid("Ffffff") == 1) 
        self.assertTrue(is_hex_colour_str_valid("123789") == 1) 
        self.assertTrue(is_hex_colour_str_valid("bc98ed") == 1) 
    def test_invalid_colour_rejected(self):
        self.assertTrue(is_hex_colour_str_valid("fffff") == 0) 
        self.assertTrue(is_hex_colour_str_valid("gfffff") == 0) 
        self.assertTrue(is_hex_colour_str_valid("fffffff") == 0) 

if __name__ == "__main__":
    unittest.main()
