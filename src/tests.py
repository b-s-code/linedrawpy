#!/usr/bin/python3
import os
import sys
import unittest
import subprocess
import linedrawpy
import main

class TestRegressions(unittest.TestCase):
    """
    We compare PPM files.  Not PNG files.
    linedrawpy is under test.
    I.e. we're not testing any other image conversion program.
    So we just test the output of linedrawpy.
    """
    
    test_script_dir = os.path.realpath(os.path.dirname(sys.argv[0]))
    test_data_dir = f"{test_script_dir}/test_data"

    @classmethod
    def setUpClass(cls):
        print(f"Creating temp test data dir: {cls.test_data_dir}")
        subprocess.run(["mkdir", cls.test_data_dir])
    
    @classmethod
    def tearDownClass(cls):
        print(f"Removing temp test data dir: {cls.test_data_dir}")

        # Prefer this to rm -rf, given there will be no subdirs
        # to deal with.
        subprocess.run(["rm", f"{cls.test_data_dir}/*"])
        subprocess.run(["rmdir", cls.test_data_dir])

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
