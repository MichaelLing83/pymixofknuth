'''
unittest module for Octa class.
'''
import unittest

OCTA_SIZE = 64  # bits

class TestOcta(unittest.TestCase):

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
