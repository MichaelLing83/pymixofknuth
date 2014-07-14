#pylint: disable=C0103
'''
Unit test for Memory class.
'''
import unittest
from Memory import Memory
from Byte import Byte
from Wyde import Wyde
from Octa import Octa
from Tetra import Tetra
from random import randint

class TestMemory(unittest.TestCase):
    '''
    Unit test suite for Memory class.
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

    def testInit(self):
        '''
        Verify that Memory instances can be correctly initialized.
        '''
        memory = Memory()

    def testSetAndReadByte(self):
        memory = Memory()
        addresses = list()
        addresses.append(Octa(0))
        addresses.append(Octa(2**64-1))
        for i in range(20):
            addresses.append(Octa(randint(0+1, 2**64-1-1)))
        for address in addresses:
            v = Byte(randint(0, 2**8-1))
            memory.set(address, v)
            self.assertEqual(memory.read(address, Byte), v)

    def testSetAndReadWydeNormal(self):
        memory = Memory()
        addresses = list()
        addresses.append(Octa(0))
        addresses.append(Octa(2**64-2))
        for i in range(20):
            addresses.append(Octa(randint(0+1, 2**64-2-1)))
        for address in addresses:
            v = Wyde(randint(0, 2**16-1))
            memory.set(address, v)
            self.assertEqual(memory.read(address, Wyde), v)
            self.assertEqual(memory.read(address, Byte), Byte(v.uint>>8))

    def testSetAndReadWydeSpecial(self):
        memory = Memory()
        memory.set(Octa(0x01), Byte(0x12))
        self.assertEqual(memory.read(Octa(0x00), Wyde), Wyde(0x0012))

    def testSetAndReadTetra(self):
        memory = Memory()
        addresses = list()
        addresses.append(Octa(0))
        addresses.append(Octa(2**64-4))
        for i in range(20):
            addresses.append(Octa(randint(0+1, 2**64-4-1)))
        for address in addresses:
            v = Tetra(randint(0, 2**32-1))
            memory.set(address, v)
            self.assertEqual(memory.read(address, Tetra), v)

    def testSetAndReadOcta(self):
        memory = Memory()
        addresses = list()
        addresses.append(Octa(0))
        addresses.append(Octa(2**64-8))
        for i in range(20):
            addresses.append(Octa(randint(0+1, 2**64-8-1)))
        for address in addresses:
            v = Octa(randint(0, 2**64-1))
            memory.set(address, v)
            self.assertEqual(memory.read(address, Octa), v)

    def test_to_str(self):
        '''
        Verify
        '''
        # by Byte
        memory = Memory()
        memory.set(Octa(0x1), Byte(0x01))
        memory.set(Octa(0x5), Byte(0x02))
        result = '''...
0x0000000000000001:\t0x01
...
0x0000000000000005:\t0x02
...
'''
        #print()
        #print(memory.print_by_byte().__repr__())
        #print("=================================")
        #print(result.__repr__())
        self.assertEqual(memory.to_str(Byte), result)

        # by Wyde
        memory = Memory()
        memory.set(Octa(0x1), Wyde(0x1234))
        memory.set(Octa(0x5), Wyde(0x2345))
        memory.set(Octa(0x7), Wyde(0x3456))
        result = '''0x0000000000000000:\t0x0012
0x0000000000000002:\t0x3400
0x0000000000000004:\t0x0023
0x0000000000000006:\t0x4534
0x0000000000000008:\t0x5600
...
'''
        #print()
        #print(memory.print_by_wyde().__repr__())
        #print("=================================")
        #print(result.__repr__())
        self.assertEqual(memory.to_str(Wyde), result)

        result = '''0x0000000000000000:\t0x00123400
0x0000000000000004:\t0x00234534
0x0000000000000008:\t0x56000000
...
'''
        # print()
        # print(memory.to_str(Tetra).__repr__())
        # print("=================================")
        # print(result.__repr__())
        self.assertEqual(memory.to_str(Tetra), result)

        result = '''0x0000000000000000:\t0x0012340000234534
0x0000000000000008:\t0x5600000000000000
...
'''
        # print()
        # print(memory.to_str(Tetra).__repr__())
        # print("=================================")
        # print(result.__repr__())
        self.assertEqual(memory.to_str(Octa), result)

if __name__ == '__main__':
    unittest.main()
