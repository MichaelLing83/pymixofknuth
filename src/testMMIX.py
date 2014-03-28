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
    
    def test__LDB_direct__(self):
        '''
        Verify that "LDB $X, $Y, Z" can load signed Byte M[$Y+Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z = Byte(int=-2)    # an direct operator
        mmix.memory.setByte(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int), Byte(int=-5))
        mmix.__LDB_direct__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].int, mmix.memory.readByte(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int)).int)
    
    def test__LDB_indirect__(self):
        '''
        Verify that "LDB $X, $Y, $Z" can load signed Byte M[$Y+$Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z, Z_value = Byte(int=-2), Octa(uint=4)
        mmix.general_purpose_registers[Z.uint].update(uint=Z_value.uint)  # set content of $Z
        mmix.memory.setByte(Octa(uint=5+4), Byte(int=-5))
        mmix.__LDB_indirect__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].int, mmix.memory.readByte(Octa(uint=5+4)).int)
    
    def test__LDBU_direct__(self):
        '''
        Verify that "LDBU $X, $Y, Z" can load unsigned Byte M[$Y+Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z = Byte(int=-2)    # an direct operator
        mmix.memory.setByte(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int), Byte(int=99))
        mmix.__LDBU_direct__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].uint, mmix.memory.readByte(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int)).uint)
    
    def test__LDBU_indirect__(self):
        '''
        Verify that "LDBU $X, $Y, $Z" can load unsigned Byte M[$Y+$Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z, Z_value = Byte(int=-2), Octa(uint=4)
        mmix.general_purpose_registers[Z.uint].update(uint=Z_value.uint)  # set content of $Z
        mmix.memory.setByte(Octa(uint=5+4), Byte(int=99))
        mmix.__LDBU_indirect__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].uint, mmix.memory.readByte(Octa(uint=5+4)).uint)
    
    def test__LDW_direct__(self):
        '''
        Verify that "LDW $X, $Y, Z" can load signed Wyde M[$Y+Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z = Byte(int=-2)    # an direct operator
        mmix.memory.setWyde(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int), Wyde(int=-5))
        mmix.__LDW_direct__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].int, mmix.memory.readWyde(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int)).int)
    
    def test__LDW_indirect__(self):
        '''
        Verify that "LDW $X, $Y, $Z" can load signed Wyde M[$Y+$Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z, Z_value = Byte(int=-2), Octa(uint=4)
        mmix.general_purpose_registers[Z.uint].update(uint=Z_value.uint)  # set content of $Z
        mmix.memory.setWyde(Octa(uint=5+4), Wyde(int=-5))
        mmix.__LDW_indirect__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].int, mmix.memory.readWyde(Octa(uint=5+4)).int)
    
    def test__LDWU_direct__(self):
        '''
        Verify that "LDWU $X, $Y, Z" can load unsigned Wyde M[$Y+Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z = Byte(int=-2)    # an direct operator
        mmix.memory.setWyde(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int), Wyde(int=99))
        mmix.__LDWU_direct__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].uint, mmix.memory.readWyde(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int)).uint)
    
    def test__LDWU_indirect__(self):
        '''
        Verify that "LDWU $X, $Y, $Z" can load unsigned Wyde M[$Y+$Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z, Z_value = Byte(int=-2), Octa(uint=4)
        mmix.general_purpose_registers[Z.uint].update(uint=Z_value.uint)  # set content of $Z
        mmix.memory.setWyde(Octa(uint=5+4), Wyde(int=99))
        mmix.__LDWU_indirect__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].uint, mmix.memory.readWyde(Octa(uint=5+4)).uint)
    
    def test__LDT_direct__(self):
        '''
        Verify that "LDT $X, $Y, Z" can load signed Tetra M[$Y+Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z = Byte(int=-2)    # an direct operator
        mmix.memory.setTetra(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int), Tetra(int=-5))
        mmix.__LDT_direct__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].int, mmix.memory.readTetra(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int)).int)
    
    def test__LDT_indirect__(self):
        '''
        Verify that "LDT $X, $Y, $Z" can load signed Tetra M[$Y+$Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z, Z_value = Byte(int=-2), Octa(uint=4)
        mmix.general_purpose_registers[Z.uint].update(uint=Z_value.uint)  # set content of $Z
        mmix.memory.setTetra(Octa(uint=5+4), Tetra(int=-5))
        mmix.__LDT_indirect__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].int, mmix.memory.readTetra(Octa(uint=5+4)).int)
    
    def test__LDTU_direct__(self):
        '''
        Verify that "LDTU $X, $Y, Z" can load unsigned Tetra M[$Y+Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z = Byte(int=-2)    # an direct operator
        mmix.memory.setTetra(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int), Tetra(int=99))
        mmix.__LDTU_direct__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].uint, mmix.memory.readTetra(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int)).uint)
    
    def test__LDTU_indirect__(self):
        '''
        Verify that "LDTU $X, $Y, $Z" can load unsigned Tetra M[$Y+$Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z, Z_value = Byte(int=-2), Octa(uint=4)
        mmix.general_purpose_registers[Z.uint].update(uint=Z_value.uint)  # set content of $Z
        mmix.memory.setTetra(Octa(uint=5+4), Tetra(int=99))
        mmix.__LDTU_indirect__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].uint, mmix.memory.readTetra(Octa(uint=5+4)).uint)
    
    def test__LDO_direct__(self):
        '''
        Verify that "LDO $X, $Y, Z" can load signed Octa M[$Y+Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z = Byte(int=-2)    # an direct operator
        mmix.memory.setOcta(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int), Octa(int=-5))
        mmix.__LDO_direct__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].int, mmix.memory.readOcta(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int)).int)
    
    def test__LDO_indirect__(self):
        '''
        Verify that "LDO $X, $Y, $Z" can load signed Octa M[$Y+$Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z, Z_value = Byte(int=-2), Octa(uint=4)
        mmix.general_purpose_registers[Z.uint].update(uint=Z_value.uint)  # set content of $Z
        mmix.memory.setOcta(Octa(uint=5+4), Octa(int=-5))
        mmix.__LDO_indirect__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].int, mmix.memory.readOcta(Octa(uint=5+4)).int)
    
    def test__LDOU_direct__(self):
        '''
        Verify that "LDOU $X, $Y, Z" can load unsigned Octa M[$Y+Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z = Byte(int=-2)    # an direct operator
        mmix.memory.setOcta(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int), Octa(int=99))
        mmix.__LDOU_direct__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].uint, mmix.memory.readOcta(Octa(uint=mmix.general_purpose_registers[Y.uint].uint+Z.int)).uint)
    
    def test__LDOU_indirect__(self):
        '''
        Verify that "LDOU $X, $Y, $Z" can load unsigned Octa M[$Y+$Z] into register $X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z, Z_value = Byte(int=-2), Octa(uint=4)
        mmix.general_purpose_registers[Z.uint].update(uint=Z_value.uint)  # set content of $Z
        mmix.memory.setOcta(Octa(uint=5+4), Octa(int=99))
        mmix.__LDOU_indirect__(X, Y, Z)
        self.assertEqual(mmix.general_purpose_registers[X.uint].uint, mmix.memory.readOcta(Octa(uint=5+4)).uint)
    
    def test__LDHT_indirect__(self):
        '''
        Verify that "LDHT $X, $Y, $Z|Z" can load Tetra into the most significant half of general_purpose_register X.
        '''
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z, Z_value = Byte(int=-2), Octa(uint=4)
        mmix.general_purpose_registers[Z.uint].update(uint=Z_value.uint)  # set content of $Z
        mmix.memory.setTetra(Octa(uint=5-2), Tetra(int=0x12345678))
        mmix.__LDHT__(X, Y, Z, isDirect=True)
        self.assertEqual(mmix.general_purpose_registers[X.uint].uint, 0x1234567800000000)
        
        mmix = MMIX()
        X = Byte(uint=1)    # index of general_purpose_registers
        mmix.general_purpose_registers[X.uint].update(uint=0x0102030405060708)  # set content of $X to some value
        Y, Y_value = Byte(uint=3), Octa(uint=5) # index of general_purpose_registers and its content
        mmix.general_purpose_registers[Y.uint].update(uint=Y_value.uint)  # set content of $Y
        Z, Z_value = Byte(int=-2), Octa(uint=4)
        mmix.general_purpose_registers[Z.uint].update(uint=Z_value.uint)  # set content of $Z
        mmix.memory.setTetra(Octa(uint=5+4), Tetra(int=0x12345678))
        mmix.__LDHT__(X, Y, Z, isDirect=False)
        self.assertEqual(mmix.general_purpose_registers[X.uint].uint, 0x1234567800000000)

if __name__ == '__main__':
    unittest.main()