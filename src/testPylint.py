#!/usr/bin/env python3
# pylint: disable=C0103
'''
Run pylint over all *.py source codes.
'''
import unittest
from os import getcwd, chdir
import subprocess
import pickle
import re
from copy import deepcopy
import argparse
from contextlib import contextmanager

# parse command line arguments
class Args: # pylint: disable=R0903
    '''
    Class used to save command line argument parsing results, and some global parameters.
    '''
    def __init__(self):
        raise Exception("Args class should not be instantiated!")

parser = argparse.ArgumentParser(description='Parse some command line arguments.')
parser.add_argument('-f', '--file', help='Python file to check.', default=None)
parser.parse_args(namespace=Args)

@contextmanager
def shell_cmd_output(shell_cmd):
    '''
    Execute a shell command using subprocess module, and return its full output (STDOUT and
    STDERR) as a string.
    '''
    try:
        stdout = subprocess.check_output(shell_cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as err:
        yield err.output.decode("utf-8")
    else:
        yield stdout.decode("utf-8")

class TestPylint(unittest.TestCase): # pylint: disable=R0904
    '''
    unittest TC to run pylint over all src/*.py files, and check rating doesn't decrease.
    '''
    previous_dir = None
    @classmethod
    def setUpClass(cls):
        print("\nStart testing %s" % __name__)
        TestPylint.previous_dir = getcwd()
        if not getcwd().endswith("src"):
            chdir("src")
        TestPylint.pylint_scores = dict()
        with open(".pylint_scores", 'rb') as f:
            TestPylint.pylint_scores = pickle.load(f)
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
            print(''.join(
                (
                    '{:30}'.format(py_file),
                    '{:+.2} -> '.format(TestPylint.previous_pylint_scores[py_file]/100),
                    '{:+.2}'.format(TestPylint.pylint_scores[py_file]/100)
                )
            ))
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
        pyfiles_to_check = list()
        with shell_cmd_output('git status -s') as git_o:
            for line in git_o.split('\n'):
                m = re.search(r"M\s+([\w\d_]+\.py)", line)
                if m:
                    pyfiles_to_check.append(m.group(1))
        #for pyfile in glob.glob('*.py'):
        for pyfile in pyfiles_to_check:
            score = -200
            # get pylint rating of current file
            print()
            with shell_cmd_output('pylint --rcfile=.pylintrc %s' % pyfile) as pylint_o:
                print('pylint --rcfile=.pylintrc %s' % pyfile)
                score = TestPylint.__get_pylint_score__(pylint_o.split('\n'))
            try:
                self.assertGreaterEqual(score, TestPylint.pylint_scores.get(pyfile, score))
            except AssertionError as err:
                print("ERROR: pylint rating of {filename} has decreased!".format(filename=pyfile))
                raise err # failed due to pylint rating degradation
            # check passes, then save the new (higher or equal) score
            TestPylint.pylint_scores[pyfile] = score

    @classmethod
    def __get_pylint_score__(cls, lines):
        # Your code has been rated at -10.62/10
        for line in lines:
            m = re.search(r"Your code has been rated at (\-?\d+\.\d+)/10", line)
            if m:
                score = m.group(1)
                if score[0] == '-':
                    return -1 * int(float(score[1:])*100)
                else:
                    return int(float(score)*100)
        return -2000    # -20.00/10

if __name__ == '__main__':
    if not Args.file: # pylint: disable=E1101
        # called from unittest or without --file argument
        unittest.main()
    else:
        with shell_cmd_output("pylint --rcfile=.pylintrc %s" % Args.file) as pylint_o: # pylint: disable=E1101
            print(pylint_o)
