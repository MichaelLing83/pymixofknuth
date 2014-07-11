import unittest
from bitstring import BitArray
from Utilities import MmixException
from Byte import Byte
from Wyde import Wyde
from Tetra import Tetra
from Octa import Octa
from random import randint
from Numeric import Range

all_classes = (Byte, Wyde, Tetra, Octa)
size_in_bit = {
    Byte: 8,
    Wyde: 16,
    Tetra: 32,
    Octa: 64,
    }

class TestNumeric(unittest.TestCase):

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
        Verify that instances can be correctly initialized.
        '''
        for klass in all_classes:
            obj = klass()
            self.assertEqual(
                obj.length,
                size_in_bit[klass],
                "Size of one {klass} must be 8 bits, it is {length} bits instead.".format(klass=klass, length=obj.length)
            )
            self.assertEqual(
                obj.int,
                0,
                "By default, {klass} should be initialized to zero, it is {int} in decimal instead.".format(klass=klass, int=obj.int)
            )
            self.assertEqual(
                obj.bin,
                '0' * size_in_bit[klass],
                "By default, {klass} should be initialized to zero, it is {bin} in binary instead.".format(klass=klass, bin=obj.bin)
            )
            self.assertEqual(obj.hex, '0' * int(size_in_bit[klass] / 4))

        # Initialize with valid signed values
        for klass in all_classes:
            test_values = list()
            test_values.append(-2**(size_in_bit[klass]-1))
            test_values.append(2**(size_in_bit[klass]-1)-1)
            for i in range(20):
                test_values.append(randint(-2**(size_in_bit[klass]-1)+1, 2**(size_in_bit[klass]-1)-1-1))
            for i in test_values:
                reference = BitArray(int=i, length=size_in_bit[klass])
                obj = klass(i)
                self.assertEqual(obj.length, size_in_bit[klass])
                self.assertEqual(obj.int, i)
                self.assertEqual(obj.bin, reference.bin)
                self.assertEqual(obj.hex, reference.hex)

        # Initialize with valid unsigned values
        for klass in all_classes:
            test_values = list()
            test_values.append(0)
            test_values.append(2**size_in_bit[klass]-1)
            for i in range(20):
                test_values.append(randint(0+1, 2**size_in_bit[klass]-1-1))
            for i in test_values:
                reference = BitArray(uint=i, length=size_in_bit[klass])
                obj = klass(i)
                self.assertEqual(obj.length, size_in_bit[klass])
                self.assertEqual(obj.uint, i)
                self.assertEqual(obj.bin, reference.bin)
                self.assertEqual(obj.hex, reference.hex)

        # Initialize with invalid values
        for klass in all_classes:
            self.assertRaises(Exception, klass, -2**(size_in_bit[klass]-1)-1)
            self.assertRaises(Exception, klass, 2**size_in_bit[klass])

    def testLogic(self):
        '''
        Verify that all numeric classes supports logical arithmetic.
        '''
        for klass in all_classes:
            odds = 0b01
            for i in range(int(size_in_bit[klass] / 2 -1)):
                odds = (odds << 2) | 0b01
            evens = 0b10
            for i in range(int(size_in_bit[klass] / 2 -1)):
                evens = (evens << 2) | 0b10
            x = klass(odds)
            y = klass(evens)
            self.assertEqual((x & y).bin, '0' * size_in_bit[klass])
            self.assertEqual(x & y, klass())
            self.assertEqual(x | y, klass(odds | evens))
            self.assertEqual(x ^ y, klass(odds ^ evens))
            self.assertEqual((x ^ y).bin, '1' * size_in_bit[klass])

    def testAlgebra(self):
        '''
        Verify that all numeric classes support algebra arithmetic.
        '''
        for klass in all_classes:
            a = randint(-2 ** (size_in_bit[klass] - 2), 0)
            b = randint(0, 2 ** (size_in_bit[klass] - 2))
            x = klass(a)
            y = klass(b)
            self.assertEqual(x + y, klass(a + b))
            self.assertEqual(y + x, klass(a + b))
            self.assertEqual(x - y, klass(a - b))
            self.assertEqual(y - x, klass(b - a))

    def testCompare(self):
        '''
        Verify that all numeric classes support comparison of whether they're equal.
        '''
        for klass in all_classes:
            a = randint(-2 ** (size_in_bit[klass] - 2), 0)
            b = randint(0, 2 ** (size_in_bit[klass] - 2))
            x = klass(a)
            y = klass(a)
            self.assertEqual(x == y, True)
            y = klass(b)
            self.assertEqual(x == y, False)

    def testSetValue(self):
        '''
        Verify that all numeric classes support updating its object value.
        '''
        for klass in all_classes:
            a = randint(-2 ** (size_in_bit[klass] - 2), 0)
            b = randint(0, 2 ** (size_in_bit[klass] - 2))
            x = klass(a)
            x.set_value(b)
            self.assertEqual(x, klass(b))

    def testShiftLeft(self):
        '''
        Verify that all numeric classes support shifting left.
        '''
        for klass in all_classes:
            x = klass(0b01)
            for i in range(klass.SIZE_IN_BIT):
                y = x << i
                self.assertEqual(y, klass(0b01 << i))
                self.assertEqual(x, klass(0b01))
            for i in range(klass.SIZE_IN_BIT, klass.SIZE_IN_BIT + 3):
                y = x << i
                self.assertEqual(y, klass())
                self.assertEqual(x, klass(0b01))
            x = klass(0b01)
            for i in range(klass.SIZE_IN_BIT - 1):
                x <<= 1
                self.assertEqual(x, klass(0b01 << (i + 1)))
            for i in range(klass.SIZE_IN_BIT, klass.SIZE_IN_BIT + 3):
                x <<= 1
                self.assertEqual(x, klass())

    def testSetByte(self):
        '''
        Verify that set_byte works for all numeric.
        '''
        for klass in all_classes:
            # using Byte
            x = klass()
            for i in range(klass.SIZE_IN_BYTE):
                x.set_byte(i, Byte(0xad))
                tmp = x.uint >> ((klass.SIZE_IN_BYTE - i - 1) * Byte.SIZE_IN_BIT)
                tmp = tmp & 0xff
                self.assertEqual(tmp ^ 0xad, 0)

    def testGetByteBySlicing(self):
        '''
        Verify that get_byte works for all numeric.
        '''
        for klass in all_classes:
            x = klass(int('1234567890abcdef'[:klass.SIZE_IN_BYTE], 16))
            for i in range(klass.SIZE_IN_BYTE):
                tmp = x.slice(i, Byte)
                tmp = tmp.uint << ((klass.SIZE_IN_BYTE - i - 1) * Byte.SIZE_IN_BIT)
                mask = 0xff << ((klass.SIZE_IN_BYTE - i - 1) * Byte.SIZE_IN_BIT)
                self.assertEqual(int('1234567890abcdef'[:klass.SIZE_IN_BYTE], 16) & mask, tmp)

    def testSlice(self):
        '''
        Verify that slice works for all numeric.
        '''
        self.assertEqual(Byte(0x12).slice(0, Byte), Byte(0x12))
        self.assertEqual(Wyde(0x1234).slice(1, Byte), Byte(0x34))
        self.assertEqual(Tetra(0x12345678).slice(1, Wyde), Wyde(0x3456))
        self.assertEqual(Octa(0x1234567890abcdef).slice(3, Tetra), Tetra(0x7890abcd))
    
    def testUpdate(self):
        '''
        Verify that update works for all numeric.
        '''
        self.assertEqual(Byte(0x12).update(0, Byte(0x34)), Byte(0x34))
        self.assertEqual(Wyde(0x1234).update(0, Byte(0x34)), Wyde(0x3434))
        self.assertEqual(Wyde(0x1234).update(1, Byte(0x12)), Wyde(0x1212))
        self.assertEqual(Tetra(0x12345678).update(1, Wyde(0x0987)), Tetra(0x12098778))

class TestRange(unittest.TestCase):

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

    def testRange(self):
        '''
        Verify that range works.
        '''
        for klass in all_classes:
            count = 0
            for obj in Range(klass, 0, 10, 1):
                self.assertEqual(obj, klass(count))
                count += 1

if __name__ == '__main__':
    unittest.main()
