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
        return self.memory.read(address, Tetra)

    @typecheck
    def _die(self, *args, **kwargs):
        '''
        Terminate MMIX machine.
        '''
        raise MmixException("MMIX died.")

    @typecheck
    def __init_instruction_table(self) -> nothing:
        '''
        Initialize instruction table according to MMIC-doc.
        '''
        self._instruction_table = dict()
        self._instruction_table[0x00] = self._die
        self._instruction_table[0x01] = self._die
        self._instruction_table[0x02] = self._die
        self._instruction_table[0x03] = self._die
        self._instruction_table[0x04] = self._die
        self._instruction_table[0x05] = self._die
        self._instruction_table[0x06] = self._die
        self._instruction_table[0x07] = self._die
        self._instruction_table[0x08] = self._die
        self._instruction_table[0x09] = self._die
        self._instruction_table[0x0a] = self._die
        self._instruction_table[0x0b] = self._die
        self._instruction_table[0x0c] = self._die
        self._instruction_table[0x0d] = self._die
        self._instruction_table[0x0e] = self._die
        self._instruction_table[0x0f] = self._die
        self._instruction_table[0x10] = self._die
        self._instruction_table[0x11] = self._die
        self._instruction_table[0x12] = self._die
        self._instruction_table[0x13] = self._die
        self._instruction_table[0x14] = self._die
        self._instruction_table[0x15] = self._die
        self._instruction_table[0x16] = self._die
        self._instruction_table[0x17] = self._die
        self._instruction_table[0x18] = self._die
        self._instruction_table[0x19] = self._die
        self._instruction_table[0x1a] = self._die
        self._instruction_table[0x1b] = self._die
        self._instruction_table[0x1c] = self._die
        self._instruction_table[0x1d] = self._die
        self._instruction_table[0x1e] = self._die
        self._instruction_table[0x1f] = self._die
        self._instruction_table[0x20] = self._die
        self._instruction_table[0x21] = self._die
        self._instruction_table[0x22] = self._die
        self._instruction_table[0x23] = self._die
        self._instruction_table[0x24] = self._die
        self._instruction_table[0x25] = self._die
        self._instruction_table[0x26] = self._die
        self._instruction_table[0x27] = self._die
        self._instruction_table[0x28] = self._die
        self._instruction_table[0x29] = self._die
        self._instruction_table[0x2a] = self._die
        self._instruction_table[0x2b] = self._die
        self._instruction_table[0x2c] = self._die
        self._instruction_table[0x2d] = self._die
        self._instruction_table[0x2e] = self._die
        self._instruction_table[0x2f] = self._die
        self._instruction_table[0x30] = self._die
        self._instruction_table[0x31] = self._die
        self._instruction_table[0x32] = self._die
        self._instruction_table[0x33] = self._die
        self._instruction_table[0x34] = self._die
        self._instruction_table[0x35] = self._die
        self._instruction_table[0x36] = self._die
        self._instruction_table[0x37] = self._die
        self._instruction_table[0x38] = self._die
        self._instruction_table[0x39] = self._die
        self._instruction_table[0x3a] = self._die
        self._instruction_table[0x3b] = self._die
        self._instruction_table[0x3c] = self._die
        self._instruction_table[0x3d] = self._die
        self._instruction_table[0x3e] = self._die
        self._instruction_table[0x3f] = self._die
        self._instruction_table[0x40] = self._die
        self._instruction_table[0x41] = self._die
        self._instruction_table[0x42] = self._die
        self._instruction_table[0x43] = self._die
        self._instruction_table[0x44] = self._die
        self._instruction_table[0x45] = self._die
        self._instruction_table[0x46] = self._die
        self._instruction_table[0x47] = self._die
        self._instruction_table[0x48] = self._die
        self._instruction_table[0x49] = self._die
        self._instruction_table[0x4a] = self._die
        self._instruction_table[0x4b] = self._die
        self._instruction_table[0x4c] = self._die
        self._instruction_table[0x4d] = self._die
        self._instruction_table[0x4e] = self._die
        self._instruction_table[0x4f] = self._die
        self._instruction_table[0x50] = self._die
        self._instruction_table[0x51] = self._die
        self._instruction_table[0x52] = self._die
        self._instruction_table[0x53] = self._die
        self._instruction_table[0x54] = self._die
        self._instruction_table[0x55] = self._die
        self._instruction_table[0x56] = self._die
        self._instruction_table[0x57] = self._die
        self._instruction_table[0x58] = self._die
        self._instruction_table[0x59] = self._die
        self._instruction_table[0x5a] = self._die
        self._instruction_table[0x5b] = self._die
        self._instruction_table[0x5c] = self._die
        self._instruction_table[0x5d] = self._die
        self._instruction_table[0x5e] = self._die
        self._instruction_table[0x5f] = self._die
        self._instruction_table[0x60] = self._die
        self._instruction_table[0x61] = self._die
        self._instruction_table[0x62] = self._die
        self._instruction_table[0x63] = self._die
        self._instruction_table[0x64] = self._die
        self._instruction_table[0x65] = self._die
        self._instruction_table[0x66] = self._die
        self._instruction_table[0x67] = self._die
        self._instruction_table[0x68] = self._die
        self._instruction_table[0x69] = self._die
        self._instruction_table[0x6a] = self._die
        self._instruction_table[0x6b] = self._die
        self._instruction_table[0x6c] = self._die
        self._instruction_table[0x6d] = self._die
        self._instruction_table[0x6e] = self._die
        self._instruction_table[0x6f] = self._die
        self._instruction_table[0x70] = self._die
        self._instruction_table[0x71] = self._die
        self._instruction_table[0x72] = self._die
        self._instruction_table[0x73] = self._die
        self._instruction_table[0x74] = self._die
        self._instruction_table[0x75] = self._die
        self._instruction_table[0x76] = self._die
        self._instruction_table[0x77] = self._die
        self._instruction_table[0x78] = self._die
        self._instruction_table[0x79] = self._die
        self._instruction_table[0x7a] = self._die
        self._instruction_table[0x7b] = self._die
        self._instruction_table[0x7c] = self._die
        self._instruction_table[0x7d] = self._die
        self._instruction_table[0x7e] = self._die
        self._instruction_table[0x7f] = self._die
        self._instruction_table[0x80] = self._die
        self._instruction_table[0x81] = self._die
        self._instruction_table[0x82] = self._die
        self._instruction_table[0x83] = self._die
        self._instruction_table[0x84] = self._die
        self._instruction_table[0x85] = self._die
        self._instruction_table[0x86] = self._die
        self._instruction_table[0x87] = self._die
        self._instruction_table[0x88] = self._die
        self._instruction_table[0x89] = self._die
        self._instruction_table[0x8a] = self._die
        self._instruction_table[0x8b] = self._die
        self._instruction_table[0x8c] = self._die
        self._instruction_table[0x8d] = self._die
        self._instruction_table[0x8e] = self._die
        self._instruction_table[0x8f] = self._die
        self._instruction_table[0x90] = self._die
        self._instruction_table[0x91] = self._die
        self._instruction_table[0x92] = self._die
        self._instruction_table[0x93] = self._die
        self._instruction_table[0x94] = self._die
        self._instruction_table[0x95] = self._die
        self._instruction_table[0x96] = self._die
        self._instruction_table[0x97] = self._die
        self._instruction_table[0x98] = self._die
        self._instruction_table[0x99] = self._die
        self._instruction_table[0x9a] = self._die
        self._instruction_table[0x9b] = self._die
        self._instruction_table[0x9c] = self._die
        self._instruction_table[0x9d] = self._die
        self._instruction_table[0x9e] = self._die
        self._instruction_table[0x9f] = self._die
        self._instruction_table[0xa0] = self._die
        self._instruction_table[0xa1] = self._die
        self._instruction_table[0xa2] = self._die
        self._instruction_table[0xa3] = self._die
        self._instruction_table[0xa4] = self._die
        self._instruction_table[0xa5] = self._die
        self._instruction_table[0xa6] = self._die
        self._instruction_table[0xa7] = self._die
        self._instruction_table[0xa8] = self._die
        self._instruction_table[0xa9] = self._die
        self._instruction_table[0xaa] = self._die
        self._instruction_table[0xab] = self._die
        self._instruction_table[0xac] = self._die
        self._instruction_table[0xad] = self._die
        self._instruction_table[0xae] = self._die
        self._instruction_table[0xaf] = self._die
        self._instruction_table[0xb0] = self._die
        self._instruction_table[0xb1] = self._die
        self._instruction_table[0xb2] = self._die
        self._instruction_table[0xb3] = self._die
        self._instruction_table[0xb4] = self._die
        self._instruction_table[0xb5] = self._die
        self._instruction_table[0xb6] = self._die
        self._instruction_table[0xb7] = self._die
        self._instruction_table[0xb8] = self._die
        self._instruction_table[0xb9] = self._die
        self._instruction_table[0xba] = self._die
        self._instruction_table[0xbb] = self._die
        self._instruction_table[0xbc] = self._die
        self._instruction_table[0xbd] = self._die
        self._instruction_table[0xbe] = self._die
        self._instruction_table[0xbf] = self._die
        self._instruction_table[0xc0] = self._die
        self._instruction_table[0xc1] = self._die
        self._instruction_table[0xc2] = self._die
        self._instruction_table[0xc3] = self._die
        self._instruction_table[0xc4] = self._die
        self._instruction_table[0xc5] = self._die
        self._instruction_table[0xc6] = self._die
        self._instruction_table[0xc7] = self._die
        self._instruction_table[0xc8] = self._die
        self._instruction_table[0xc9] = self._die
        self._instruction_table[0xca] = self._die
        self._instruction_table[0xcb] = self._die
        self._instruction_table[0xcc] = self._die
        self._instruction_table[0xcd] = self._die
        self._instruction_table[0xce] = self._die
        self._instruction_table[0xcf] = self._die
        self._instruction_table[0xd0] = self._die
        self._instruction_table[0xd1] = self._die
        self._instruction_table[0xd2] = self._die
        self._instruction_table[0xd3] = self._die
        self._instruction_table[0xd4] = self._die
        self._instruction_table[0xd5] = self._die
        self._instruction_table[0xd6] = self._die
        self._instruction_table[0xd7] = self._die
        self._instruction_table[0xd8] = self._die
        self._instruction_table[0xd9] = self._die
        self._instruction_table[0xda] = self._die
        self._instruction_table[0xdb] = self._die
        self._instruction_table[0xdc] = self._die
        self._instruction_table[0xdd] = self._die
        self._instruction_table[0xde] = self._die
        self._instruction_table[0xdf] = self._die
        self._instruction_table[0xe0] = self._die
        self._instruction_table[0xe1] = self._die
        self._instruction_table[0xe2] = self._die
        self._instruction_table[0xe3] = self._die
        self._instruction_table[0xe4] = self._die
        self._instruction_table[0xe5] = self._die
        self._instruction_table[0xe6] = self._die
        self._instruction_table[0xe7] = self._die
        self._instruction_table[0xe8] = self._die
        self._instruction_table[0xe9] = self._die
        self._instruction_table[0xea] = self._die
        self._instruction_table[0xeb] = self._die
        self._instruction_table[0xec] = self._die
        self._instruction_table[0xed] = self._die
        self._instruction_table[0xee] = self._die
        self._instruction_table[0xef] = self._die
        self._instruction_table[0xf0] = self._die
        self._instruction_table[0xf1] = self._die
        self._instruction_table[0xf2] = self._die
        self._instruction_table[0xf3] = self._die
        self._instruction_table[0xf4] = self._die
        self._instruction_table[0xf5] = self._die
        self._instruction_table[0xf6] = self._die
        self._instruction_table[0xf7] = self._die
        self._instruction_table[0xf8] = self._die
        self._instruction_table[0xf9] = self._die
        self._instruction_table[0xfa] = self._die
        self._instruction_table[0xfb] = self._die
        self._instruction_table[0xfc] = self._die
        self._instruction_table[0xfd] = self._die
        self._instruction_table[0xfe] = self._die
        self._instruction_table[0xff] = self._die

    @typecheck
    def __execute_instruction__(self, instruction: Tetra) -> nothing:
        '''
        Execute one MMIX machine instruction.
        '''
        pass

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
    def __print_memory__(self, unit: one_of((Byte, Wyde, Tetra, Octa))=Byte) -> str:
        '''
        Print current memory to a string. Can be used for debugging purpose.

        @unit=Byte (class): which class to use as printing granuity.

        @return (str): a string representation of current memory.
        '''
        return self.memory.to_str(unit)

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
            memory_addr = Octa(self.general_purpose_registers[Y.uint].uint+Z.int)
        else:
            memory_addr = Octa(self.general_purpose_registers[Y.uint].uint + self.general_purpose_registers[Z.uint].int)
        if is_signed:
            tmp = self.memory.read(memory_addr, data_type).int
            self.general_purpose_registers[X.uint].set_value(tmp)
        else:
            tmp = self.memory.read(memory_addr, data_type).uint
            self.general_purpose_registers[X.uint].set_value(tmp)

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
            memory_addr = Octa(self.general_purpose_registers[Y.uint].uint+Z.int)
        else:
            memory_addr = Octa(self.general_purpose_registers[Y.uint].uint+self.general_purpose_registers[Z.uint].int)
        tmp = self.memory.read(memory_addr, Tetra).uint
        self.general_purpose_registers[X.uint].set_value(tmp<<(Octa.SIZE_IN_BIT - Tetra.SIZE_IN_BIT))

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
            memory_addr = Octa(self.general_purpose_registers[Y.uint].uint+Z.int)
        else:
            memory_addr = Octa(self.general_purpose_registers[Y.uint].uint+self.general_purpose_registers[Z.uint].int)
        self.general_purpose_registers[X.uint].set_value(memory_addr.uint)

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
            memory_addr = Octa(self.general_purpose_registers[Y.uint].uint + Z.int)
        else:
            memory_addr = Octa(self.general_purpose_registers[Y.uint].uint + self.general_purpose_registers[Z.uint].int)
        if is_signed:
            # TODO: overflow check needs to be added.
            tmp = self.general_purpose_registers[X.uint].uint & 0xFF
            self.memory.set(memory_addr, Byte(tmp))
        else:
            tmp = self.general_purpose_registers[X.uint].uint & 0xFF
            self.memory.set(memory_addr, Byte(tmp))

    @typecheck
    def __STB__(self, X: Byte, Y: Byte, Z: Byte, is_direct: bool) -> nothing:
        '''
        '''
        self.__STx__(X, Y, Z, Byte, True, is_direct)
