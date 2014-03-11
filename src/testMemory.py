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
    
    def testSetAndReadWyde(self):
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
    
    def test__read_instruction__(self):
        pass

if __name__ == '__main__':
    unittest.main()