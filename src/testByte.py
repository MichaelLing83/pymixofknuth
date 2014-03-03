import unittest
from bitstring import BitArray
from bitstring import CreationError
from Byte import Byte

BYTE_SIZE = 8

class TestByte(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testInit(self):
        '''
        Verify that Byte instances can be correctly initialized.
        '''
        byte = Byte()
        self.assertEqual(byte.length, BYTE_SIZE, "Size of one Byte must be 8 bits, it is %d bits instead." % byte.length)
        self.assertEqual(byte.int, 0, "By default, Byte should be initialized to zero, it is %d in decimal instead." % byte.int)
        self.assertEqual(byte.bin, '00000000', "By default, Byte should be initialized to zero, it is %s in binary instead." % byte.bin)
        self.assertEqual(byte.hex, '00')
        
        # Initialize with valid signed values
        for i in range(-2**(BYTE_SIZE-1), 2**(BYTE_SIZE-1)):
            reference = BitArray(int=i, length=BYTE_SIZE)
            byte = Byte(int=i)
            self.assertEqual(byte.length, BYTE_SIZE)
            self.assertEqual(byte.int, i)
            self.assertEqual(byte.bin, reference.bin)
            self.assertEqual(byte.hex, reference.hex)
        
        # Initialize with valid unsigned values
        for i in range(0, 2**BYTE_SIZE):
            reference = BitArray(uint=i, length=BYTE_SIZE)
            byte = Byte(uint=i)
            self.assertEqual(byte.length, BYTE_SIZE)
            self.assertEqual(byte.uint, i)
            self.assertEqual(byte.bin, reference.bin)
            self.assertEqual(byte.hex, reference.hex)
        
        # Initialize with invalid values
        self.assertRaises(CreationError, Byte, int=-2**(BYTE_SIZE-1)-1)
        self.assertRaises(CreationError, Byte, int=2**(BYTE_SIZE-1))
        self.assertRaises(CreationError, Byte, uint=-1)
        self.assertRaises(CreationError, Byte, uint=2**BYTE_SIZE)
    
    def testLogic(self):
        '''
        Verify that Byte supports logical arithmetic.
        '''
        x = Byte(uint=0b01010101)
        y = Byte(uint=0b10101010)
        self.assertEqual((x&y).bin, '00000000')
        self.assertEqual((x|y).bin, '11111111')
        self.assertEqual((x^y).bin, '11111111')
    
    def testAlgebra(self):
        '''
        Verify that Byte supports algebra arithmetic.
        '''
        x = Byte(uint=2)
        y = Byte(uint=3)
        self.assertEqual((x+y).uint, 5)
        self.assertEqual((y+x).int, 5)
        self.assertEqual((x-y).int, -1)
        self.assertEqual((y-x).int, 1)

if __name__ == '__main__':
    unittest.main()