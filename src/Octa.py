from bitstring import BitArray
from Utilities import guarantee
from Numeric import Numeric
from Byte import Byte
from typecheck import *

class Octa(Numeric):
    '''
    '''
    
    SIZE_IN_BIT = 64   # bits
    SIZE_IN_BYTE = int(SIZE_IN_BIT/Byte.SIZE_IN_BIT)    # 8 Byte
    
    @typecheck
    def __init__(self, *args, **kwargs) -> nothing:
        self.octa = self._genBitString(Octa.SIZE_IN_BIT, *args, **kwargs)
        self.length = self.octa.length
        self.int = self.octa.int
        self.uint = self.octa.uint
        self.bin = self.octa.bin
        self.hex = self.octa.hex
    
    def __and__(self, another_Octa):
        return Octa(uint=(self.octa & another_Octa.octa).uint)
    
    def __or__(self, another_Octa):
        return Octa(uint=(self.octa | another_Octa.octa).uint)
    
    def __xor__(self, another_Octa):
        return Octa(uint=(self.octa ^ another_Octa.octa).uint)
    
    def __add__(self, another_Octa):
        return Octa(int=(self.octa.int + another_Octa.octa.int))
    
    def __sub__(self, another_Octa):
        return Octa(int=(self.octa.int - another_Octa.octa.int))
    
    def __eq__(self, another_Octa):
        return self.octa.uint == another_Octa.octa.uint
