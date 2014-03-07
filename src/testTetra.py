import unittest
from bitstring import BitArray
from bitstring import CreationError
from Tetra import Tetra
from random import randint

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
    
    def testInit(self):
        '''
        Verify that Tetra instances can be correctly initialized.
        '''
        tetra = Tetra()
        self.assertEqual(tetra.length, TETRA_SIZE, "Size of one Tetra must be %d bits, it is %d bits instead." % (TETRA_SIZE, tetra.length))
        self.assertEqual(tetra.int, 0, "By default, Tetra should be initialized to zero, it is %d in decimal instead." % tetra.int)
        self.assertEqual(tetra.bin, '0'*TETRA_SIZE, "By default, Tetra should be initialized to zero, it is %s in binary instead." % tetra.bin)
        self.assertEqual(tetra.hex, '0'*int(TETRA_SIZE/4))
        
        # Initialize with valid signed values
        test_values = list()
        test_values.append(-2**(TETRA_SIZE-1))
        test_values.append(2**(TETRA_SIZE-1)-1)
        for i in range(20):
            test_values.append(randint(-2**(TETRA_SIZE-1)+1, 2**(TETRA_SIZE-1)-1-1))
        for i in test_values:
            reference = BitArray(int=i, length=TETRA_SIZE)
            tetra = Tetra(int=i)
            self.assertEqual(tetra.length, TETRA_SIZE)
            self.assertEqual(tetra.int, i)
            self.assertEqual(tetra.bin, reference.bin)
            self.assertEqual(tetra.hex, reference.hex)
        
        # Initialize with valid unsigned values
        test_values = list()
        test_values.append(0)
        test_values.append(2**TETRA_SIZE-1)
        for i in range(20):
            test_values.append(randint(0+1, 2**TETRA_SIZE-1-1))
        for i in test_values:
            reference = BitArray(uint=i, length=TETRA_SIZE)
            tetra = Tetra(uint=i)
            self.assertEqual(tetra.length, TETRA_SIZE)
            self.assertEqual(tetra.uint, i)
            self.assertEqual(tetra.bin, reference.bin)
            self.assertEqual(tetra.hex, reference.hex)
        
        # Initialize with invalid values
        self.assertRaises(CreationError, Tetra, int=-2**(TETRA_SIZE-1)-1)
        self.assertRaises(CreationError, Tetra, int=2**(TETRA_SIZE-1))
        self.assertRaises(CreationError, Tetra, uint=-1)
        self.assertRaises(CreationError, Tetra, uint=2**TETRA_SIZE)
    
    def testLogic(self):
        '''
        Verify that Tetra supports logical arithmetic.
        '''
        x = Tetra(uint=0b01010101)
        y = Tetra(uint=0b10101010)
        self.assertEqual((x&y).bin, '0'*TETRA_SIZE)
        self.assertEqual((x|y).bin, '0'*(TETRA_SIZE-8)+'11111111')
        self.assertEqual((x^y).bin, '0'*(TETRA_SIZE-8)+'11111111')
    
    def testAlgebra(self):
        '''
        Verify that Tetra supports algebra arithmetic.
        '''
        x = Tetra(uint=2)
        y = Tetra(uint=3)
        self.assertEqual((x+y).uint, 5)
        self.assertEqual((y+x).int, 5)
        self.assertEqual((x-y).int, -1)
        self.assertEqual((y-x).int, 1)

if __name__ == '__main__':
    unittest.main()