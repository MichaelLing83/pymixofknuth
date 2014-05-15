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
        self._bitstring = self._genBitString(Octa.SIZE_IN_BIT, *args, **kwargs)
        self.length = self._bitstring.length
        self.int = self._bitstring.int
        self.uint = self._bitstring.uint
        self.bin = self._bitstring.bin
        self.hex = self._bitstring.hex
