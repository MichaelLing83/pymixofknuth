from Register import Register
from Memory import Memory

class MMIX:
    ADDRESS_WIDTH_IN_BIT = 64
    REGISTER_BIT_WIDTH = 64
    def __init__(self):
        # add registers
        self.general_purpose_registers = list()
        for i in range(256):
            self.general_purpose_registers.append(Register())
        self.special_purpose_registers = list()
        for i in range(32):
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