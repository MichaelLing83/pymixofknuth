'''
MMIX computer simulator.
'''
from Register import Register
from Memory import Memory
from Byte import Byte
from Wyde import Wyde
from Tetra import Tetra
from Octa import Octa
from typecheck import *

class Instruction:
    '''
    Representing one MMIX instruction. It's always four bytes:
        Instruc, X, Y, Z
    '''
    @typecheck
    def __init__(self, instruct: Octa, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        Initialize one MMIX instruction object.

        @instruct (Octa): address of the most important byte (big-endian)

        @return (Tetra): an four-byte instruction
        '''

class MMIX:
    '''
    A class representing a MMIX machine.
    '''
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
        self.special_purpose_register_names = (
            'rB', 'rD', 'rE', 'rH', 'rJ', 'rM', 'rR', 'rBB', 'rC', 'rN', 'rO', 'rS', 'rI', 'rT',
            'rTT', 'rK', 'rQ', 'rU', 'rV', 'rG', 'rL', 'rA', 'rF', 'rP', 'rW', 'rX', 'rY', 'rZ',
            'rWW', 'rXX', 'rYY', 'rZZ'
            )

        # add memory
        self.memory = Memory()

    @typecheck
    def __read_instruction__(self, address: Octa) -> Tetra:
        '''
        Read one MMIX instruction, whose most important byte starts from given address.

        @address (Octa): address of the most important byte (big-endian)

        @return (Tetra): an four-byte instruction
        '''
        return self.memory.readTetra(address)

    @typecheck
    def __get_special_register_index_by_name__(self, special_purpose_register_name: str) -> int:
        '''
        Get index of special purpose register by its name.

        @address (str): name of a special purpose register, e.g. 'rA'

        @return (int): index into self.special_purpose_registers
        '''
        for i in range(len(self.special_purpose_register_names)):
            if special_purpose_register_name == self.special_purpose_register_names[i]:
                return i
        raise Exception("Special purpose register: %s is not defined." % special_purpose_register_name)

    @typecheck
    def __print_memory__(self, unit=Byte) -> str:
        '''
        Print current memory to a string. Can be used for debugging purpose.

        @unit=Byte (class): which class to use as printing granuity, Byte or Wyde.

        @return (str): a string representation of current memory.
        '''
        if unit == Byte:
            return self.memory.print_by_byte()
        elif unit == Wyde:
            return self.memory.print_by_wyde()
        else:
            raise Exception("Given memory unit=%s is not supported!" % unit)

    @typecheck
    def __print_general_purpose_registers__(self) -> str:
        '''
        Print all general_purpose_registers to a string. Can be used for debugging purpose.

        @return (str): a string representation of all general_purpose_registers.
        '''
        result = str()
        for register_index in range(len(self.general_purpose_registers)):
            result += ''.join(("%s:\t0x" % hex(register_index) + self.general_purpose_registers[register_index].hex + "\n"))
        return result

    @typecheck
    def __print_special_purpose_registers__(self) -> str:
        '''
        Print all special_purpose_registers to a string. Can be used for debugging purpose.

        @return (str): a string representation of all special_purpose_registers.
        '''
        result = str()
        for register_index in range(len(self.special_purpose_registers)):
            result += "%s:\t0x"%self.special_purpose_register_names[register_index] + self.special_purpose_registers[register_index].hex + "\n"
        return result

    @typecheck
    def __LDB_direct__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        s(M[$Y + Z]) is loaded into register X as a signed number between −128 and +127, inclusive.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Byte, is_signed=True, is_direct=True)

    @typecheck
    def __LDB_indirect__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        s(M[$Y + $Z]) is loaded into register X as a signed number between −128 and +127, inclusive.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Byte, is_signed=True, is_direct=False)

    @typecheck
    def __LDBU_direct__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        u(M[$Y + Z]) is loaded into register X as a unsigned number between 0 and 255, inclusive.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Byte, is_signed=False, is_direct=True)

    @typecheck
    def __LDBU_indirect__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        u(M[$Y + $Z]) is loaded into register X as a unsigned number between 0 and 255, inclusive.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Byte, is_signed=False, is_direct=False)

    @typecheck
    def __LDW_direct__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        s(M[$Y + Z]) is loaded into register X as a signed Wyde.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Wyde, is_signed=True, is_direct=True)

    @typecheck
    def __LDW_indirect__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        s(M[$Y + $Z]) is loaded into register X as a signed Wyde.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Wyde, is_signed=True, is_direct=False)

    @typecheck
    def __LDWU_direct__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        u(M[$Y + Z]) is loaded into register X as a unsigned Wyde.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Wyde, is_signed=False, is_direct=True)

    @typecheck
    def __LDWU_indirect__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        u(M[$Y + $Z]) is loaded into register X as a unsigned Wyde.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Wyde, is_signed=False, is_direct=False)

    @typecheck
    def __LDT_direct__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        s(M[$Y + Z]) is loaded into register X as a signed Tetra.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Tetra, is_signed=True, is_direct=True)

    @typecheck
    def __LDT_indirect__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        s(M[$Y + $Z]) is loaded into register X as a signed Tetra.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Tetra, is_signed=True, is_direct=False)

    @typecheck
    def __LDTU_direct__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        u(M[$Y + Z]) is loaded into register X as a unsigned Tetra.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Tetra, is_signed=False, is_direct=True)

    @typecheck
    def __LDTU_indirect__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        u(M[$Y + $Z]) is loaded into register X as a unsigned Tetra.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Tetra, is_signed=False, is_direct=False)

    @typecheck
    def __LDx__(self, X: Byte, Y: Byte, Z: Byte, data_type: one_of((Byte, Wyde, Tetra, Octa)), is_signed: bool, is_direct: bool) -> nothing:
        '''
        Load data from memory into general_purpose_register X. How big chunk of data is loaded is
        based on data_type. Whether Z is a direct operator or an indirect operator depends on
        is_direct.
        M[$Y + $Z] or M[$Y + Z] is loaded into register X using given data_type.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;
        @data_type (class): data type to load, must be one of Byte, Wyde, Tetra, or Octa;
        @is_signed (bool): whether to use signed value or not;
        @is_direct (bool): whether Z is an direct operator or not.

        @return (None)
        '''
        if is_direct:
            memory_addr = Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)
        else:
            memory_addr = Octa(uint=self.general_purpose_registers[Y.uint].uint + self.general_purpose_registers[Z.uint].int)
        if is_signed:
            tmp = self.memory.read(memory_addr, data_type).int
            self.general_purpose_registers[X.uint].update(int=tmp)
        else:
            tmp = self.memory.read(memory_addr, data_type).uint
            self.general_purpose_registers[X.uint].update(uint=tmp)

    @typecheck
    def __LDO_direct__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        s(M[$Y + Z]) is loaded into register X as a signed Tetra.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Octa, is_signed=True, is_direct=True)

    @typecheck
    def __LDO_indirect__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        s(M[$Y + $Z]) is loaded into register X as a signed Tetra.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Octa, is_signed=True, is_direct=False)

    @typecheck
    def __LDOU_direct__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        u(M[$Y + Z]) is loaded into register X as a unsigned Tetra.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator.

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Octa, is_signed=False, is_direct=True)

    @typecheck
    def __LDOU_indirect__(self, X: Byte, Y: Byte, Z: Byte) -> nothing:
        '''
        u(M[$Y + $Z]) is loaded into register X as a unsigned Tetra.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;

        @return (None)
        '''
        self.__LDx__(X, Y, Z, Octa, is_signed=False, is_direct=False)

    @typecheck
    def __LDHT__(self, X: Byte, Y: Byte, Z: Byte, is_direct: bool) -> nothing:
        '''
        Load high Tetra
        Bytes M_4[$Y + $Z] or M_4[$Y + Z] are loaded into the most significant half of register X, and the least
        significant half is cleared to zero. (One use of “high tetra arithmetic” is to detect overflow easily when
        tetrabytes are added or subtracted.)

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator or an index to general_purpose_registers;
        @is_direct (bool): whether Z is an direct operator or not.

        @return (None)
        '''
        if is_direct:
            memory_addr = Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)
        else:
            memory_addr = Octa(uint=self.general_purpose_registers[Y.uint].uint+self.general_purpose_registers[Z.uint].int)
        tmp = self.memory.readTetra(memory_addr).uint
        self.general_purpose_registers[X.uint].update(int=tmp<<(Octa.SIZE_IN_BIT - Tetra.SIZE_IN_BIT))

    @typecheck
    def __LDA__(self, X: Byte, Y: Byte, Z: Byte, is_direct: bool) -> nothing:
        '''
        Load address.
        The address $Y + $Z or $Y + Z is loaded into register X. This instruction is simply another name for the
        ADDU instruction discussed below; it can be used when the programmer is thinking of memory addresses
        instead of numbers. The MMIX assembler converts LDA into the same OP-code as ADDU.

        @X (Byte): Index to general_purpose_registers;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): A direct operator or an index to general_purpose_registers;
        @is_direct (bool): whether Z is an direct operator or not.

        @return (None)
        '''
        if is_direct:
            memory_addr = Octa(uint=self.general_purpose_registers[Y.uint].uint+Z.int)
        else:
            memory_addr = Octa(uint=self.general_purpose_registers[Y.uint].uint+self.general_purpose_registers[Z.uint].int)
        self.general_purpose_registers[X.uint].update(uint=memory_addr.uint)

    @typecheck
    def __STx__(self, X: Byte, Y: Byte, Z: Byte, data_type: one_of((Byte, Wyde, Tetra, Octa)), is_signed: bool, is_direct: bool) -> nothing:
        '''
        Store registers into memory. How big chunk of data is loaded is based on data_type. Whether Z is a direct operator or an indirect
        operator depends on is_direct.
        register X is stored to M[$Y + $Z] or M[$Y + Z] using given data_type.

        @X (Byte): Index to general_purpose_registers, which to be stored;
        @Y (Byte): Index to general_purpose_registers;
        @Z (Byte): Index to general_purpose_registers;
        @data_type (class): data type to load, must be one of Byte, Wyde, Tetra, or Octa;
        @is_signed (bool): whether to use signed value or not;
        @is_direct (bool): whether Z is an direct operator or not.

        @return (None)
        '''
        if is_direct:
            memory_addr = Octa(uint=self.general_purpose_registers[Y.uint].uint + Z.int)
        else:
            memory_addr = Octa(uint=self.general_purpose_registers[Y.uint].uint + self.general_purpose_registers[Z.uint].int)
        if is_signed:
            # TODO: overflow check needs to be added.
            tmp = self.general_purpose_registers[X.uint].uint & Byte(uint=0xFF)
            self.memory.set(memory_addr, Byte, Byte(uint=tmp))
        else:
            tmp = self.general_purpose_registers[X.uint].uint & Byte(uint=0xFF)
            self.memory.set(memory_addr, Byte, Byte(uint=tmp))
