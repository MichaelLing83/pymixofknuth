import unittest
from bitstring import BitArray
from Utilities import MmixException
from Octa import Octa
from random import randint

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
    
    def testInit(self):
        '''
        Verify that Octa instances can be correctly initialized.
        '''
        octa = Octa()
        self.assertEqual(octa.length, OCTA_SIZE, "Size of one Octa must be %d bits, it is %d bits instead." % (OCTA_SIZE, octa.length))
        self.assertEqual(octa.int, 0, "By default, Octa should be initialized to zero, it is %d in decimal instead." % octa.int)
        self.assertEqual(octa.bin, '0'*OCTA_SIZE, "By default, Octa should be initialized to zero, it is %s in binary instead." % octa.bin)
        self.assertEqual(octa.hex, '0'*int(OCTA_SIZE/4))
        
        # Initialize with valid signed values
        test_values = list()
        test_values.append(-2**(OCTA_SIZE-1))
        test_values.append(2**(OCTA_SIZE-1)-1)
        for i in range(20):
            test_values.append(randint(-2**(OCTA_SIZE-1)+1, 2**(OCTA_SIZE-1)-1-1))
        for i in test_values:
            reference = BitArray(int=i, length=OCTA_SIZE)
            octa = Octa(int=i)
            self.assertEqual(octa.length, OCTA_SIZE)
            self.assertEqual(octa.int, i)
            self.assertEqual(octa.bin, reference.bin)
            self.assertEqual(octa.hex, reference.hex)
        
        # Initialize with valid unsigned values
        test_values = list()
        test_values.append(0)
        test_values.append(2**OCTA_SIZE-1)
        for i in range(20):
            test_values.append(randint(0+1, 2**OCTA_SIZE-1-1))
        for i in test_values:
            reference = BitArray(uint=i, length=OCTA_SIZE)
            octa = Octa(uint=i)
            self.assertEqual(octa.length, OCTA_SIZE)
            self.assertEqual(octa.uint, i)
            self.assertEqual(octa.bin, reference.bin)
            self.assertEqual(octa.hex, reference.hex)
        
        # Initialize with invalid values
        self.assertRaises(MmixException, Octa, int=-2**(OCTA_SIZE-1)-1)
        self.assertRaises(MmixException, Octa, int=2**(OCTA_SIZE-1))
        self.assertRaises(MmixException, Octa, uint=-1)
        self.assertRaises(MmixException, Octa, uint=2**OCTA_SIZE)
    
    def testLogic(self):
        '''
        Verify that Octa supports logical arithmetic.
        '''
        x = Octa(uint=0b01010101)
        y = Octa(uint=0b10101010)
        self.assertEqual((x&y).bin, '0'*OCTA_SIZE)
        self.assertEqual((x|y).bin, '0'*(OCTA_SIZE-8)+'11111111')
        self.assertEqual((x^y).bin, '0'*(OCTA_SIZE-8)+'11111111')
    
    def testAlgebra(self):
        '''
        Verify that Octa supports algebra arithmetic.
        '''
        x = Octa(uint=2)
        y = Octa(uint=3)
        self.assertEqual((x+y).uint, 5)
        self.assertEqual((y+x).int, 5)
        self.assertEqual((x-y).int, -1)
        self.assertEqual((y-x).int, 1)
    
    def testUpdateValue(self):
        x = Octa(uint=2)
        x.update(uint=5)
        self.assertEqual(x.int, 5)
        self.assertEqual(x.bin, '0'*61+'101')
        self.assertEqual(x.hex, '00'*7+'05')

if __name__ == '__main__':
    unittest.main()