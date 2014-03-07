import unittest
from Memory import Memory
from Byte import Byte
from Octa import Octa
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

if __name__ == '__main__':
    unittest.main()