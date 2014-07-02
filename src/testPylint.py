import unittest
from os import getcwd, chdir
import subprocess
import glob
import pickle
import re
from copy import deepcopy

class TestPylint(unittest.TestCase):
    previous_dir = None
    @classmethod
    def setUpClass(cls):
        print("\nStart testing %s" % __name__)
        TestPylint.previous_dir = getcwd()
        if not getcwd().endswith("src"):
            chdir("src")
        TestPylint.pylint_scores = dict()
        try:
            f = open(".pylint_scores", 'rb')
            TestPylint.pylint_scores = pickle.load(f)
            f.close()
        except IOError as err:
            # This is the first time, we don't have any historical reference
            pass
        TestPylint.previous_pylint_scores = deepcopy(TestPylint.pylint_scores)

    @classmethod
    def tearDownClass(cls):
        f = open(".pylint_scores", 'wb')
        pickle.dump(TestPylint.pylint_scores, f, pickle.HIGHEST_PROTOCOL)
        f.close()
        all_py_files = list(TestPylint.pylint_scores.keys())
        all_py_files.sort()
        print()
        for py_file in all_py_files:
            print(''.join(('{:30}'.format(py_file), '{:+.2} -> '.format(TestPylint.previous_pylint_scores[py_file]/100), '{:+.2}'.format(TestPylint.pylint_scores[py_file]/100))))
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
        for pyfile in glob.glob('*.py'):
            score = -200
            # get pylint rating of current file
            try:
                pylint_o = subprocess.check_output("pylint --rcfile=.pylintrc %s" % pyfile, shell=True, stderr=subprocess.STDOUT)
                score = self.__get_pylint_score__(pylint_o.decode("utf-8").split('\n'))
            except subprocess.CalledProcessError as err:
                score = self.__get_pylint_score__(err.output.decode("utf-8").split('\n'))
            # check it's not lower than before
            try:
                self.assertGreaterEqual(score, TestPylint.pylint_scores.get(pyfile, score))
            except AssertionError as err:
                print("ERROR: pylint rating of {filename} has decreased!".format(filename=pyfile))
                raise err
            # check passes, then save the new (higher or equal) score
            TestPylint.pylint_scores[pyfile] = score
    
    def __get_pylint_score__(self, lines):
        # Your code has been rated at -10.62/10
        for line in lines:
            m = re.search("Your code has been rated at (\-?\d+\.\d+)/10", line)
            if m:
                score = m.group(1)
                if score[0] == '-':
                    return -1 * int(float(score[1:])*100)
                else:
                    return int(float(score)*100)
        return -2000    # -20.00/10

if __name__ == '__main__':
    unittest.main()
