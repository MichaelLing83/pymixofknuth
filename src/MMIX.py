﻿from Register import Register
from Memory import Memory
from Byte import Byte
from Wyde import Wyde
from Octa import Octa

class MMIX:
    ADDRESS_WIDTH_IN_BIT = 64
    REGISTER_BIT_WIDTH = 64
    NUM_OF_GENERAL_PURPOSE_REGISTER = 256
    NUM_OF_SPECIAL_PURPOSE_REGISTER = 32
    def __init__(self):
        # add registers
        self.general_purpose_registers = list()
        for i in range(MMIX.NUM_OF_GENERAL_PURPOSE_REGISTER):
            self.general_purpose_registers.append(Register())
        self.special_purpose_registers = list()
        for i in range(MMIX.NUM_OF_SPECIAL_PURPOSE_REGISTER):
            self.special_purpose_registers.append(Register())
        self.special_purpose_register_names = ('rB', 'rD', 'rE', 'rH', 'rJ', 'rM', 'rR', 'rBB', 'rC', 'rN', 'rO', 'rS', 'rI', 'rT', 'rTT', 'rK', 'rQ', 'rU', 'rV', 'rG', 'rL', 'rA', 'rF', 'rP', 'rW', 'rX', 'rY', 'rZ', 'rWW', 'rXX', 'rYY', 'rZZ')
        
        # add memory
        self.memory = Memory()
    
    def __read_instruction__(self, address):
        '''
        Read one MMIX instruction, whose most important byte starts from given address.

        @address (Octa): address of the most important byte (big-endian)

        @return (Tetra): an four-byte instruction
        '''
        return self.memory.readTetra(address)
    
    def __get_special_register_index_by_name__(self, special_purpose_register_name):
        '''
        Get index of special purpose register by its name.

        @address (str): name of a special purpose register, e.g. 'rA'

        @return (int): index into self.special_purpose_registers
        '''
        for i in range(len(self.special_purpose_register_names)):
            if special_purpose_register_name == self.special_purpose_register_names[i]:
                return i
        raise Exception("Special purpose register name: %s is not defined." % special_purpose_register_name)
    
    def __print_memory__(self, unit=Byte):
        '''
        Print current memory to a string. Can be used for debugging purpose.

        @unit=Byte (class): which class to use as printing granuity, Byte or Wyde.

        @return (str): a string representation of current memory.
        '''
        if unit==Byte:
            return self.memory.print_by_byte()
        elif unit==Wyde:
            return self.memory.print_by_wyde()
        else:
            raise Exception("Given memory unit=%s is not supported!" % unit)
    
    def __print_general_purpose_registers__(self):
        '''
        Print all general_purpose_registers to a string. Can be used for debugging purpose.

        @return (str): a string representation of all general_purpose_registers.
        '''
        result = str()
        for register_index in range(len(self.general_purpose_registers)):
            result += "%s:\t0x"%hex(register_index) + self.general_purpose_registers[register_index].hex + "\n"
        return result
    
    def __print_special_purpose_registers__(self):
        '''
        Print all special_purpose_registers to a string. Can be used for debugging purpose.

        @return (str): a string representation of all special_purpose_registers.
        '''
        result = str()
        for register_index in range(len(self.special_purpose_registers)):
            result += "%s:\t0x"%self.special_purpose_register_names[register_index] + self.special_purpose_registers[register_index].hex + "\n"
        return result
    
    def __LDB_direct__(self, X, Y, Z):
        '''
        s(M[$Y + Z]) is loaded into register X as a signed number between −128 and +127, inclusive.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        tmp = self.memory.readByte(Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)).int
        #print("==========DEBUG==========")
        #print("tmp=%d" % tmp)
        #print("Y=%d, Z=%d" % (Y.uint, Z.int))
        #print("$Y=0x%s" % self.general_purpose_registers[Y.uint].hex)
        #print("memory[$Y+Z]=memory[0x%s]=0x%s" % (Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int).hex, self.memory.readByte(Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)).hex))
        #print("==========DEBUG==========")
        self.general_purpose_registers[X.uint].update(int=tmp)
    
    def __LDB_indirect__(self, X, Y, Z):
        '''
        s(M[$Y + $Z]) is loaded into register X as a signed number between −128 and +127, inclusive.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        tmp = self.memory.readByte(Octa(uint=self.general_purpose_registers[Y.uint].uint+self.general_purpose_registers[Z.uint].uint)).int
        #print("==========DEBUG==========")
        #print("tmp=%d" % tmp)
        #print("Y=%d, Z=%d" % (Y.uint, Z.int))
        #print("$Y=0x%s" % self.general_purpose_registers[Y.uint].hex)
        #print("memory[$Y+Z]=memory[0x%s]=0x%s" % (Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int).hex, self.memory.readByte(Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)).hex))
        #print("==========DEBUG==========")
        self.general_purpose_registers[X.uint].update(int=tmp)
    
    def __LDBU_direct__(self, X, Y, Z):
        '''
        u(M[$Y + Z]) is loaded into register X as a unsigned number between 0 and 255, inclusive.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        tmp = self.memory.readByte(Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)).uint
        #print("==========DEBUG==========")
        #print("tmp=%d" % tmp)
        #print("Y=%d, Z=%d" % (Y.uint, Z.int))
        #print("$Y=0x%s" % self.general_purpose_registers[Y.uint].hex)
        #print("memory[$Y+Z]=memory[0x%s]=0x%s" % (Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int).hex, self.memory.readByte(Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)).hex))
        #print("==========DEBUG==========")
        self.general_purpose_registers[X.uint].update(uint=tmp)
    
    def __LDBU_indirect__(self, X, Y, Z):
        '''
        u(M[$Y + $Z]) is loaded into register X as a unsigned number between 0 and 255, inclusive.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        tmp = self.memory.readByte(Octa(uint=self.general_purpose_registers[Y.uint].uint+self.general_purpose_registers[Z.uint].uint)).uint
        #print("==========DEBUG==========")
        #print("tmp=%d" % tmp)
        #print("Y=%d, Z=%d" % (Y.uint, Z.int))
        #print("$Y=0x%s" % self.general_purpose_registers[Y.uint].hex)
        #print("memory[$Y+Z]=memory[0x%s]=0x%s" % (Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int).hex, self.memory.readByte(Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)).hex))
        #print("==========DEBUG==========")
        self.general_purpose_registers[X.uint].update(uint=tmp)
    
    def __LDW_direct__(self, X, Y, Z):
        '''
        s(M[$Y + Z]) is loaded into register X as a signed Wyde.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        tmp = self.memory.readWyde(Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)).int
        self.general_purpose_registers[X.uint].update(int=tmp)
    
    def __LDW_indirect__(self, X, Y, Z):
        '''
        s(M[$Y + $Z]) is loaded into register X as a signed Wyde.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        tmp = self.memory.readWyde(Octa(uint=self.general_purpose_registers[Y.uint].uint+self.general_purpose_registers[Z.uint].uint)).int
        self.general_purpose_registers[X.uint].update(int=tmp)
    
    def __LDWU_direct__(self, X, Y, Z):
        '''
        u(M[$Y + Z]) is loaded into register X as a unsigned Wyde.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        tmp = self.memory.readWyde(Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)).uint
        self.general_purpose_registers[X.uint].update(uint=tmp)
    
    def __LDWU_indirect__(self, X, Y, Z):
        '''
        u(M[$Y + $Z]) is loaded into register X as a unsigned Wyde.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        tmp = self.memory.readWyde(Octa(uint=self.general_purpose_registers[Y.uint].uint+self.general_purpose_registers[Z.uint].uint)).uint
        self.general_purpose_registers[X.uint].update(uint=tmp)
    
    def __LDT_direct__(self, X, Y, Z):
        '''
        s(M[$Y + Z]) is loaded into register X as a signed Tetra.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        tmp = self.memory.readTetra(Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)).int
        self.general_purpose_registers[X.uint].update(int=tmp)
    
    def __LDT_indirect__(self, X, Y, Z):
        '''
        s(M[$Y + $Z]) is loaded into register X as a signed Tetra.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        tmp = self.memory.readTetra(Octa(uint=self.general_purpose_registers[Y.uint].uint+self.general_purpose_registers[Z.uint].uint)).int
        self.general_purpose_registers[X.uint].update(int=tmp)
    
    def __LDTU_direct__(self, X, Y, Z):
        '''
        u(M[$Y + Z]) is loaded into register X as a unsigned Tetra.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        tmp = self.memory.readTetra(Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)).uint
        self.general_purpose_registers[X.uint].update(uint=tmp)
    
    def __LDTU_indirect__(self, X, Y, Z):
        '''
        u(M[$Y + $Z]) is loaded into register X as a unsigned Tetra.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        tmp = self.memory.readTetra(Octa(uint=self.general_purpose_registers[Y.uint].uint+self.general_purpose_registers[Z.uint].uint)).uint
        self.general_purpose_registers[X.uint].update(uint=tmp)
    
    def __LDx__(self, X, Y, Z, dataType, isSigned, isDirect):
        '''
        Load data from memory into general_purpose_register X. How big chunk of data is loaded is based on dataType. Whether Z is a direct operator or an indirect operator depends on isDirect.
        M[$Y + $Z] or M[$Y + Z] is loaded into register X using given dataType.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;
        @dataType (class): data type to load, must be one of Byte, Wyde, Tetra, or Octa;
        @isSigned (bool): whether to use signed value or not;
        @isDirect (bool): whether Z is an direct operator or not.

        @return (None)
        '''
        if isDirect:
            memory_addr = Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)
        else:
            memory_addr = Octa(uint=self.general_purpose_registers[Y.uint].uint+self.general_purpose_registers[Z.uint].int)
        if isSigned:
            tmp = self.memory.read(memory_addr, dataType).int
            self.general_purpose_registers[X.uint].update(int=tmp)
        else:
            tmp = self.memory.read(memory_addr, dataType).uint
            self.general_purpose_registers[X.uint].update(uint=tmp)
    
    def __LDO_direct__(self, X, Y, Z):
        '''
        s(M[$Y + Z]) is loaded into register X as a signed Tetra.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Octa, isSigned=True, isDirect=True)
    
    def __LDO_indirect__(self, X, Y, Z):
        '''
        s(M[$Y + $Z]) is loaded into register X as a signed Tetra.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Octa, isSigned=True, isDirect=False)
    
    def __LDOU_direct__(self, X, Y, Z):
        '''
        u(M[$Y + Z]) is loaded into register X as a unsigned Tetra.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Octa, isSigned=False, isDirect=True)
    
    def __LDOU_indirect__(self, X, Y, Z):
        '''
        u(M[$Y + $Z]) is loaded into register X as a unsigned Tetra.
        
        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Octa, isSigned=False, isDirect=False)