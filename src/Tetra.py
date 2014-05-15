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
        self._bitstring = self._genBitString(Tetra.SIZE_IN_BIT, *args, **kwargs)
        self.length = self._bitstring.length
        self.int = self._bitstring.int
        self.uint = self._bitstring.uint
        self.bin = self._bitstring.bin
        self.hex = self._bitstring.hex
