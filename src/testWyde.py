import unittest
from bitstring import BitArray
from bitstring import CreationError
from Wyde import Wyde
from random import randint

WYDE_SIZE = 16  # bits

class TestWyde(unittest.TestCase):

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
        Verify that Wyde instances can be correctly initialized.
        '''
        wyde = Wyde()
        self.assertEqual(Wyde.SIZE_IN_BYTE, 2)
        self.assertEqual(wyde.length, WYDE_SIZE, "Size of one Wyde must be %d bits, it is %d bits instead." % (WYDE_SIZE, wyde.length))
        self.assertEqual(wyde.int, 0, "By default, Wyde should be initialized to zero, it is %d in decimal instead." % wyde.int)
        self.assertEqual(wyde.bin, '0'*WYDE_SIZE, "By default, Wyde should be initialized to zero, it is %s in binary instead." % wyde.bin)
        self.assertEqual(wyde.hex, '0'*int(WYDE_SIZE/4))
        
        # Initialize with valid signed values
        test_values = list()
        test_values.append(-2**(WYDE_SIZE-1))
        test_values.append(2**(WYDE_SIZE-1)-1)
        for i in range(20):
            test_values.append(randint(-2**(WYDE_SIZE-1)+1, 2**(WYDE_SIZE-1)-1-1))
        for i in test_values:
            reference = BitArray(int=i, length=WYDE_SIZE)
            wyde = Wyde(int=i)
            self.assertEqual(wyde.length, WYDE_SIZE)
            self.assertEqual(wyde.int, i)
            self.assertEqual(wyde.bin, reference.bin)
            self.assertEqual(wyde.hex, reference.hex)
        
        # Initialize with valid unsigned values
        test_values = list()
        test_values.append(0)
        test_values.append(2**WYDE_SIZE-1)
        for i in range(20):
            test_values.append(randint(0+1, 2**WYDE_SIZE-1-1))
        for i in test_values:
            reference = BitArray(uint=i, length=WYDE_SIZE)
            wyde = Wyde(uint=i)
            self.assertEqual(wyde.length, WYDE_SIZE)
            self.assertEqual(wyde.uint, i)
            self.assertEqual(wyde.bin, reference.bin)
            self.assertEqual(wyde.hex, reference.hex)
        
        # Initialize with invalid values
        self.assertRaises(CreationError, Wyde, int=-2**(WYDE_SIZE-1)-1)
        self.assertRaises(CreationError, Wyde, int=2**(WYDE_SIZE-1))
        self.assertRaises(CreationError, Wyde, uint=-1)
        self.assertRaises(CreationError, Wyde, uint=2**WYDE_SIZE)
    
    def testLogic(self):
        '''
        Verify that Wyde supports logical arithmetic.
        '''
        x = Wyde(uint=0b01010101)
        y = Wyde(uint=0b10101010)
        self.assertEqual((x&y).bin, '0000000000000000')
        self.assertEqual((x|y).bin, '0000000011111111')
        self.assertEqual((x^y).bin, '0000000011111111')
    
    def testAlgebra(self):
        '''
        Verify that Wyde supports algebra arithmetic.
        '''
        x = Wyde(uint=2)
        y = Wyde(uint=3)
        self.assertEqual((x+y).uint, 5)
        self.assertEqual((y+x).int, 5)
        self.assertEqual((x-y).int, -1)
        self.assertEqual((y-x).int, 1)
    
    def testCompare(self):
        x = Wyde(uint=5)
        y = Wyde(uint=5)
        self.assertEqual(x, y)
    
    def testUpdateValue(self):
        x = Wyde(uint=0x1234)
        x.update(uint=0x2345)
        self.assertEqual(x.int, 0x2345)
        self.assertEqual(x.bin, Wyde(uint=0x2345).bin)
        self.assertEqual(x.hex, '2345')

if __name__ == '__main__':
    unittest.main()