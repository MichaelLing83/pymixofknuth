'''
unittest module for Tetra class.
'''
import unittest

TETRA_SIZE = 32  # bits

class TestTetra(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nStart testing %s" % __name__)

    @classmethod
    def tearDownClass(cls):
        print("\nFinish testing %s" % __name__)

    def setUp(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
