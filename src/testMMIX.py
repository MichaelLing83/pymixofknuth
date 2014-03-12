import unittest
from Octa import Octa
from Byte import Byte
from Wyde import Wyde
from Tetra import Tetra
from Register import Register
from MMIX import MMIX

class TestMMIX(unittest.TestCase):

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
        Verify that MMIX instances can be correctly initialized.
        '''
        mmix = MMIX()
        self.assertEqual(len(mmix.general_purpose_registers), 256)
        self.assertEqual(len(mmix.special_purpose_registers), 32)
        self.assertEqual(len(mmix.special_purpose_register_names), 32)
    
    def test__read_instruction__(self):
        '''
        Verify that MMIX can read one instruction.
        '''
        mmix = MMIX()
        mmix.memory.setByte(Octa(uint=0), Byte(uint=0x31))
        mmix.memory.setByte(Octa(uint=1), Byte(uint=0x32))
        mmix.memory.setByte(Octa(uint=2), Byte(uint=0x33))
        mmix.memory.setByte(Octa(uint=3), Byte(uint=0x34))
        self.assertEqual(mmix.__read_instruction__(Octa(uint=0)), Tetra(uint=0x31323334))
    
    def test__get_special_register_index_by_name__(self):
        '''
        Verify that MMIX can find a special purpose register's index by its name.
        '''
        mmix = MMIX()
        self.assertEqual(mmix.__get_special_register_index_by_name__('rA'), 21)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rB'), 0)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rC'), 8)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rD'), 1)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rE'), 2)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rF'), 22)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rG'), 19)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rH'), 3)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rI'), 12)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rJ'), 4)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rK'), 15)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rL'), 20)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rM'), 5)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rN'), 9)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rO'), 10)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rP'), 23)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rQ'), 16)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rR'), 6)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rS'), 11)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rT'), 13)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rU'), 17)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rV'), 18)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rW'), 24)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rX'), 25)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rY'), 26)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rZ'), 27)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rBB'), 7)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rTT'), 14)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rWW'), 28)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rXX'), 29)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rYY'), 30)
        self.assertEqual(mmix.__get_special_register_index_by_name__('rZZ'), 31)
    
    def test__print_memory__(self):
        mmix = MMIX()
        mmix.memory.setOcta(Octa(uint=0x0102030405060708), Octa(uint=0x0102030405060708))
        self.assertEqual(mmix.__print_memory__(), mmix.memory.print_by_byte())
        self.assertEqual(mmix.__print_memory__(unit=Wyde), mmix.memory.print_by_wyde())
    
    def test__print_general_purpose_registers__(self):
        '''
        Verify that all general_purpose_registers can be printed for debugging.
        '''
        mmix = MMIX()
        for i in range(MMIX.NUM_OF_GENERAL_PURPOSE_REGISTER):
            mmix.general_purpose_registers[i].update(uint=i)
        result = str()
        for i in range(MMIX.NUM_OF_GENERAL_PURPOSE_REGISTER):
            result += "%s:\t0x"%hex(i) + Register(uint=i).hex + "\n"
        self.assertEqual(mmix.__print_general_purpose_registers__(), result)
    
    def test__print_special_purpose_registers__(self):
        '''
        Verify that all special_purpose_registers can be printed for debugging.
        '''
        mmix = MMIX()
        tmp_map = dict()
        tmp_map[21] = 'rA'
        tmp_map[0] = 'rB'
        tmp_map[8] = 'rC'
        tmp_map[1] = 'rD'
        tmp_map[2] = 'rE'
        tmp_map[22] = 'rF'
        tmp_map[19] = 'rG'
        tmp_map[3] = 'rH'
        tmp_map[12] = 'rI'
        tmp_map[4] = 'rJ'
        tmp_map[15] = 'rK'
        tmp_map[20] = 'rL'
        tmp_map[5] = 'rM'
        tmp_map[9] = 'rN'
        tmp_map[10] = 'rO'
        tmp_map[23] = 'rP'
        tmp_map[16] = 'rQ'
        tmp_map[6] = 'rR'
        tmp_map[11] = 'rS'
        tmp_map[13] = 'rT'
        tmp_map[17] = 'rU'
        tmp_map[18] = 'rV'
        tmp_map[24] = 'rW'
        tmp_map[25] = 'rX'
        tmp_map[26] = 'rY'
        tmp_map[27] = 'rZ'
        tmp_map[7] = 'rBB'
        tmp_map[14] = 'rTT'
        tmp_map[28] = 'rWW'
        tmp_map[29] = 'rXX'
        tmp_map[30] = 'rYY'
        tmp_map[31] = 'rZZ'
        for i in range(MMIX.NUM_OF_SPECIAL_PURPOSE_REGISTER):
            mmix.special_purpose_registers[i].update(uint=i)
        result = str()
        for i in range(MMIX.NUM_OF_SPECIAL_PURPOSE_REGISTER):
            result += "%s:\t0x"%tmp_map[i] + Register(uint=i).hex + "\n"
        self.assertEqual(mmix.__print_special_purpose_registers__(), result)

if __name__ == '__main__':
    unittest.main()