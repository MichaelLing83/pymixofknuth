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
        self.special_purpose_register_names = ['rB', 'rD', 'rE', 'rH', 'rJ', 'rM', 'rR', 'rBB', 'rC', 'rN', 'rO', 'rS', 'rI', 'rT', 'rTT', 'rK', 'rQ', 'rU', 'rV', 'rG', 'rL', 'rA', 'rF', 'rP', 'rW', 'rX', 'rY', 'rZ', 'rWW', 'rXX', 'rYY', 'rZZ']
        
        # add memory
        self.memory = Memory()