#!/usr/bin/python3
import unittest
import subprocess
import linedrawpy
import main

class TestRegressions(unittest.TestCase):
    """
    We compare PPM files.  Not PNG files.
    linedrawpy is under test.
    Not any image conversion program.
    So we just test the output of linedrawpy.
    """

    @classmethod
    def setUpClass(cls):
        subprocess.run(["mkdir", "../test_data"])
    
    @classmethod
    def setUpClass(cls):
        subprocess.run(["rm", "-rf", "../test_data"])

    def test_triangle(self):
        # TODO
        pass

if __name__ == "__main__":
    unittest.main()
