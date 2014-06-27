import unittest
from os import getcwd, chdir
import subprocess

class TestPylint(unittest.TestCase):
    previous_dir = None
    @classmethod
    def setUpClass(cls):
        print("\nStart testing %s" % __name__)
        TestPylint.previous_dir = getcwd()
        if not getcwd().endswith("src"):
            chdir("src")

    @classmethod
    def tearDownClass(cls):
        print("\nFinish testing %s" % __name__)
        chdir(TestPylint.previous_dir)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPylint(self):
        '''
        Run pylint over all source codes.
        '''
        # run pylint over all *.py files.
        try:
            pylint_o = subprocess.check_output("pylint Byte.py", shell=True, stderr=subprocess.STDOUT)
            print(pylint_o)
        except subprocess.CalledProcessError as err:
            print(err.output.decode("utf-8"))

if __name__ == '__main__':
    unittest.main()