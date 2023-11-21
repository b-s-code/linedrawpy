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

    def test_triangle_pipe(self):
        """
        Checks linedrawpy can operate on input provided
        via standard input.
        """
        # TODO
        pass
    
    def test_triangle_file(self):
        """
        Checks linedrawpy can take a filename as an
        argument and use the file's contents as input.
        """
        # TODO
        pass
    
    def test_concentric_flakes(self):
        """
        Tests linedrawpy can produce an image from a
        nontrivial edge set.
        """
        # TODO
        pass

    def test_sin_segments(self):
        """
        Tests linedrawpy can produce an image from a
        nontrivial edge set.
        """
        # TODO
        pass

    def test_layering(self):
        """
        Tests linedrawpy treats ordering of input
        edges correctly.  I.e. last edge is closest
        to top of image.
        """
        # TODO
        pass

if __name__ == "__main__":
    unittest.main()
