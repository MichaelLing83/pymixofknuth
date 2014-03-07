import unittest

class TestRegister(unittest.TestCase):
    '''
    As Octa test covers all, here are the extra tests that Register needs.
    '''
    
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