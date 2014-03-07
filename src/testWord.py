import unittest
from bitstring import BitArray
from bitstring import CreationError
from Word import Word
from random import randint

WORD_SIZE = 16  # bits

class TestWord(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testInit(self):
        '''
        Verify that Word instances can be correctly initialized.
        '''
        word = Word()
        self.assertEqual(word.length, WORD_SIZE, "Size of one Word must be %d bits, it is %d bits instead." % (WORD_SIZE, word.length))
        self.assertEqual(word.int, 0, "By default, Word should be initialized to zero, it is %d in decimal instead." % word.int)
        self.assertEqual(word.bin, '0'*WORD_SIZE, "By default, Word should be initialized to zero, it is %s in binary instead." % word.bin)
        self.assertEqual(word.hex, '0'*int(WORD_SIZE/4))
        
        # Initialize with valid signed values
        test_values = list()
        test_values.append(-2**(WORD_SIZE-1))
        test_values.append(2**(WORD_SIZE-1)-1)
        for i in range(20):
            test_values.append(randint(-2**(WORD_SIZE-1)+1, 2**(WORD_SIZE-1)-1-1))
        for i in test_values:
            reference = BitArray(int=i, length=WORD_SIZE)
            word = Word(int=i)
            self.assertEqual(word.length, WORD_SIZE)
            self.assertEqual(word.int, i)
            self.assertEqual(word.bin, reference.bin)
            self.assertEqual(word.hex, reference.hex)
        
        # Initialize with valid unsigned values
        test_values = list()
        test_values.append(0)
        test_values.append(2**WORD_SIZE-1)
        for i in range(20):
            test_values.append(randint(0+1, 2**WORD_SIZE-1-1))
        for i in test_values:
            reference = BitArray(uint=i, length=WORD_SIZE)
            word = Word(uint=i)
            self.assertEqual(word.length, WORD_SIZE)
            self.assertEqual(word.uint, i)
            self.assertEqual(word.bin, reference.bin)
            self.assertEqual(word.hex, reference.hex)
        
        # Initialize with invalid values
        self.assertRaises(CreationError, Word, int=-2**(WORD_SIZE-1)-1)
        self.assertRaises(CreationError, Word, int=2**(WORD_SIZE-1))
        self.assertRaises(CreationError, Word, uint=-1)
        self.assertRaises(CreationError, Word, uint=2**WORD_SIZE)
    
    def testLogic(self):
        '''
        Verify that Word supports logical arithmetic.
        '''
        x = Word(uint=0b01010101)
        y = Word(uint=0b10101010)
        self.assertEqual((x&y).bin, '0000000000000000')
        self.assertEqual((x|y).bin, '0000000011111111')
        self.assertEqual((x^y).bin, '0000000011111111')
    
    def testAlgebra(self):
        '''
        Verify that Word supports algebra arithmetic.
        '''
        x = Word(uint=2)
        y = Word(uint=3)
        self.assertEqual((x+y).uint, 5)
        self.assertEqual((y+x).int, 5)
        self.assertEqual((x-y).int, -1)
        self.assertEqual((y-x).int, 1)

if __name__ == '__main__':
    unittest.main()