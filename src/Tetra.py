from bitstring import BitArray
from Byte import Byte
from typecheck import *
from Utilities import guarantee
from Numeric import Numeric

class Tetra(Numeric):
    '''
    '''
    SIZE_IN_BIT = 32   # bits
    SIZE_IN_BYTE = int(SIZE_IN_BIT/Byte.SIZE_IN_BIT)    # 4 Byte
    
    @typecheck
    def __init__(self, *args, **kwargs) -> nothing:
        self.tetra = self._genBitString(Tetra.SIZE_IN_BIT, *args, **kwargs)
        self.length = self.tetra.length
        self.int = self.tetra.int
        self.uint = self.tetra.uint
        self.bin = self.tetra.bin
        self.hex = self.tetra.hex
    
    def __and__(self, another_Tetra):
        return Tetra(uint=(self.tetra & another_Tetra.tetra).uint)
    
    def __or__(self, another_Tetra):
        return Tetra(uint=(self.tetra | another_Tetra.tetra).uint)
    
    def __xor__(self, another_Tetra):
        return Tetra(uint=(self.tetra ^ another_Tetra.tetra).uint)
    
    def __add__(self, another_Tetra):
        return Tetra(int=(self.tetra.int + another_Tetra.tetra.int))
    
    def __sub__(self, another_Tetra):
        return Tetra(int=(self.tetra.int - another_Tetra.tetra.int))
    
    def __eq__(self, another_Tetra):
        return self.tetra.uint == another_Tetra.tetra.uint
