import unittest
from MMIX import MMIX

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
    
    def testInit(self):
        '''
        Verify that Octa instances can be correctly initialized.
        '''
        mmix = MMIX()
        self.assertEqual(len(mmix.general_purpose_registers), 256)
        self.assertEqual(len(mmix.special_purpose_registers), 32)
        self.assertEqual(len(mmix.special_purpose_register_names), 32)

if __name__ == '__main__':
    unittest.main()