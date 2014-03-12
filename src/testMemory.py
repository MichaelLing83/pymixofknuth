import unittest
from Memory import Memory
from Byte import Byte
from Wyde import Wyde
from Octa import Octa
from Tetra import Tetra
from random import randint

class TestMemory(unittest.TestCase):

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
        addresses.append(Octa(uint=0))
        addresses.append(Octa(uint=2**64-1))
        for i in range(20):
            addresses.append(Octa(uint=randint(0+1, 2**64-1-1)))
        for address in addresses:
            v = Byte(uint=randint(0, 2**8-1))
            memory.setByte(address, v)
            self.assertEqual(memory.readByte(address), v)
    
    def testSetAndReadWydeNormal(self):
        memory = Memory()
        addresses = list()
        addresses.append(Octa(uint=0))
        addresses.append(Octa(uint=2**64-1))
        for i in range(20):
            addresses.append(Octa(uint=randint(0+1, 2**64-1-1)))
        for address in addresses:
            v = Wyde(uint=randint(0, 2**16-1))
            memory.setWyde(address, v)
            #print(memory.readWyde(address).hex)
            #print(v.hex)
            self.assertEqual(memory.readWyde(address), v)
            self.assertEqual(memory.readByte(address), Byte(uint=v.uint>>8))
    
    def testSetAndReadWydeSpecial(self):
        memory = Memory()
        memory.setByte(Octa(uint=0x1), Byte(uint=0x12))
        self.assertEqual(memory.readWyde(Octa(uint=0x00)), Wyde(uint=0x0012))
    
    def testSetAndReadTetra(self):
        memory = Memory()
        addresses = list()
        addresses.append(Octa(uint=0))
        addresses.append(Octa(uint=2**64-1))
        for i in range(20):
            addresses.append(Octa(uint=randint(0+1, 2**64-1-1)))
        for address in addresses:
            v = Tetra(uint=randint(0, 2**32-1))
            memory.setTetra(address, v)
            #print(memory.readTetra(address).hex)
            #print(v.hex)
            self.assertEqual(memory.readTetra(address), v)
    
    def testSetAndReadOcta(self):
        memory = Memory()
        addresses = list()
        addresses.append(Octa(uint=0))
        addresses.append(Octa(uint=2**64-1))
        for i in range(20):
            addresses.append(Octa(uint=randint(0+1, 2**64-1-1)))
        for address in addresses:
            v = Octa(uint=randint(0, 2**64-1))
            memory.setOcta(address, v)
            #print(memory.readOcta(address).hex)
            #print(v.hex)
            self.assertEqual(memory.readOcta(address), v)
    
    def test_print_by_byte(self):
        '''
        Verify Memory.print_by_byte dumps memory to a readable string as a Byte array.
        '''
        memory = Memory()
        memory.setByte(Octa(uint=0x1), Byte(uint=0x01))
        memory.setByte(Octa(uint=0x5), Byte(uint=0x02))
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
        self.assertEqual(memory.print_by_byte(), result)
    
    def test_print_by_wyde(self):
        '''
        Verify Memory.print_by_wyde dumps memory to a readable string as a Wyde array. Note that it should be aligned to Wyde boundary.
        '''
        memory = Memory()
        memory.setWyde(Octa(uint=0x1), Wyde(uint=0x1234))
        memory.setWyde(Octa(uint=0x5), Wyde(uint=0x2345))
        memory.setWyde(Octa(uint=0x7), Wyde(uint=0x3456))
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
        self.assertEqual(memory.print_by_wyde(), result)

if __name__ == '__main__':
    unittest.main()