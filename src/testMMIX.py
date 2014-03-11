import unittest
from Octa import Octa
from Byte import Byte
from Tetra import Tetra
from MMIX import MMIX

class TestMMIX(unittest.TestCase):

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
        Verify that MMIX instances can be correctly initialized.
        '''
        mmix = MMIX()
        self.assertEqual(len(mmix.general_purpose_registers), 256)
        self.assertEqual(len(mmix.special_purpose_registers), 32)
        self.assertEqual(len(mmix.special_purpose_register_names), 32)
    
    def test__read_instruction__(self):
        '''
        Verify that MMIX can read one instruction.
        '''
        mmix = MMIX()
        mmix.memory.setByte(Octa(uint=0), Byte(uint=0x31))
        mmix.memory.setByte(Octa(uint=1), Byte(uint=0x32))
        mmix.memory.setByte(Octa(uint=2), Byte(uint=0x33))
        mmix.memory.setByte(Octa(uint=3), Byte(uint=0x34))
        self.assertEqual(mmix.__read_instruction__(Octa(uint=0)), Tetra(uint=0x31323334))

if __name__ == '__main__':
    unittest.main()