#!/usr/bin/python3
import os
import sys
import subprocess
import glob

# The whole program is small enough we treat it as a unit.
import unittest

class TestRegressions(unittest.TestCase):
    """
    We compare PPM files.  Not PNG files.
    linedrawpy is under test.
    I.e. we're not testing any other image conversion program.
    So we just test the output of linedrawpy.
    """
   
    # Path to directory where this test program resides..
    test_script_dir = os.path.realpath(os.path.dirname(sys.argv[0]))

    # Persisent test data.
    test_data_per_dir = f"{test_script_dir}/test_data_persistent"

    # Temporary test data.
    test_data_tmp_dir = f"{test_script_dir}/test_data_temp"
   
    # Path to the linedrawpy program.
    linedrawpy = f"{test_script_dir}/../src/main.py"
    
    @classmethod
    def setUpClass(cls):
        print(f"Creating temp test data dir: {cls.test_data_tmp_dir}")
        subprocess.run(["mkdir", cls.test_data_tmp_dir])
    
    @classmethod
    def tearDownClass(cls):
        print(f"Removing temp test data dir: {cls.test_data_tmp_dir}")

        # Prefer this to rm -rf, given there will be no subdirs
        # to deal with.

        # A literal * character gets passed to OS if we use
        # a subprocess.run(["rm", f"{cls.test_data_dir}/*"])
        # since the subprocess module does not use a shell by
        # default.  We use glob to solve this.
        files_to_remove = glob.glob(f"{cls.test_data_tmp_dir}/*")
        for deletee in files_to_remove:
            subprocess.run(["rm", deletee])

        subprocess.run(["rmdir", cls.test_data_tmp_dir])

    def test_triangle_pipe(self):
        """
        Checks linedrawpy can operate on input provided
        via standard input.
        """
        # Run pylinedraw _without_ importing its code here. 
        # Closer to actual usage scenario.
        edges = subprocess.run(
                [
                    "cat",
                    f"{self.test_data_per_dir}/edges.txt"
                ],
                capture_output=True)
        with open(f"{self.test_data_tmp_dir}/edges.ppm", "w") as edges_ppm:
           subprocess.run(
                    [self.linedrawpy],
                    input=edges.stdout,
                    stdout=edges_ppm)

        # Output has been produced, so now we can
        # just compare it to expected output.
        # There are definitely faster ways to do this.
        edges_ppm_expected = []
        edges_ppm_actual = []
        with open(f"{self.test_data_tmp_dir}/edges.ppm", "r") as edges_ppm:
            edges_ppm_actual = edges_ppm.readlines()
        with open(f"{self.test_data_per_dir}/edges.ppm", "r") as edges_ppm:
            edges_ppm_expected = edges_ppm.readlines()

        self.assertTrue(edges_ppm_actual == edges_ppm_expected)
    
    def test_triangle_file(self):
        """
        Checks linedrawpy can take a filename as an
        argument and use the file's contents as input.
        """
        # Run pylinedraw _without_ importing its code here. 
        # Closer to actual usage scenario.
        edges = subprocess.run(
                [
                    self.linedrawpy,
                    f"{self.test_data_per_dir}/edges.txt"
                ],
                capture_output=True)
        with open(f"{self.test_data_tmp_dir}/edges.ppm", "w") as edges_ppm:
           subprocess.run(
                    ["cat"],
                    input=edges.stdout,
                    stdout=edges_ppm)

        # Output has been produced, so now we can
        # just compare it to expected output.
        # There are definitely faster ways to do this.
        edges_ppm_expected = []
        edges_ppm_actual = []
        with open(f"{self.test_data_tmp_dir}/edges.ppm", "r") as edges_ppm:
            edges_ppm_actual = edges_ppm.readlines()
        with open(f"{self.test_data_per_dir}/edges.ppm", "r") as edges_ppm:
            edges_ppm_expected = edges_ppm.readlines()
        
        self.assertTrue(edges_ppm_actual == edges_ppm_expected)
    
    def test_concentric_flakes(self):
        """
        Tests linedrawpy can produce an image from a
        nontrivial edge set.
        """
        # Run pylinedraw _without_ importing its code here. 
        # Closer to actual usage scenario.
        concentric_flakes_edges = subprocess.run(
                [
                    self.linedrawpy,
                    f"{self.test_data_per_dir}/edges_concentric_flakes.txt"
                ],
                capture_output=True)
        with open(f"{self.test_data_tmp_dir}/concentric_flakes.ppm", "w") as concentric_flakes_ppm:
           subprocess.run(
                    ["cat"],
                    input=concentric_flakes_edges.stdout,
                    stdout=concentric_flakes_ppm)

        # Output has been produced, so now we can
        # just compare it to expected output.
        # There are definitely faster ways to do this.
        concentric_flakes_ppm_expected = []
        concentric_flakes_ppm_actual = []
        with open(f"{self.test_data_tmp_dir}/concentric_flakes.ppm", "r") as concentric_flakes_ppm:
            concentric_flakes_ppm_actual = concentric_flakes_ppm.readlines()
        with open(f"{self.test_data_per_dir}/concentric_flakes.ppm", "r") as concentric_flakes_ppm:
            concentric_flakes_ppm_expected = concentric_flakes_ppm.readlines()
        
        self.assertTrue(concentric_flakes_ppm_actual == concentric_flakes_ppm_expected)

    def test_layering(self):
        """
        Tests linedrawpy treats ordering of input
        edges correctly.  I.e. last edge is closest
        to top of image.
        """
        # Run pylinedraw _without_ importing its code here. 
        # Closer to actual usage scenario.
        layered_edges = subprocess.run(
                [
                    "cat",
                    f"{self.test_data_per_dir}/layered_edges.txt"
                ],
                capture_output=True)
        with open(f"{self.test_data_tmp_dir}/layered_edges.ppm", "w") as layered_edges_ppm:
           subprocess.run(
                    [self.linedrawpy],
                    input=layered_edges.stdout,
                    stdout=layered_edges_ppm)

        # Output has been produced, so now we can
        # just compare it to expected output.
        # There are definitely faster ways to do this.
        layered_edges_ppm_expected = []
        layered_edges_ppm_actual = []
        with open(f"{self.test_data_tmp_dir}/layered_edges.ppm", "r") as layered_edges_ppm:
            layered_edges_ppm_actual = layered_edges_ppm.readlines()
        with open(f"{self.test_data_per_dir}/layered_edges.ppm", "r") as layered_edges_ppm:
            layered_edges_ppm_expected = layered_edges_ppm.readlines()

        self.assertTrue(layered_edges_ppm_actual == layered_edges_ppm_expected)
        
if __name__ == "__main__":
    unittest.main()
