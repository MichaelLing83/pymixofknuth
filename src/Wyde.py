from bitstring import BitArray
from Byte import Byte
from typecheck import *
from Utilities import guarantee
from Numeric import Numeric

class Wyde(Numeric):
    '''
    '''

    SIZE_IN_BIT = 16   # bits
    SIZE_IN_BYTE = int(SIZE_IN_BIT/Byte.SIZE_IN_BIT)    # 2 Byte
    
    def __init__(self, *args, **kwargs):
        '''
        '''
        self.wyde = self._genBitString(Wyde.SIZE_IN_BIT, *args, **kwargs)
        self.length = self.wyde.length
        self.int = self.wyde.int
        self.uint = self.wyde.uint
        self.bin = self.wyde.bin
        self.hex = self.wyde.hex
    
    def __and__(self, another_Wyde):
        return Wyde(uint=(self.wyde & another_Wyde.wyde).uint)
    
    def __or__(self, another_Wyde):
        return Wyde(uint=(self.wyde | another_Wyde.wyde).uint)
    
    def __xor__(self, another_Wyde):
        return Wyde(uint=(self.wyde ^ another_Wyde.wyde).uint)
    
    def __add__(self, another_Wyde):
        return Wyde(int=(self.wyde.int + another_Wyde.wyde.int))
    
    def __sub__(self, another_Wyde):
        return Wyde(int=(self.wyde.int - another_Wyde.wyde.int))
    
    def __eq__(self, another_Wyde):
        return self.wyde.uint == another_Wyde.wyde.uint
    
    def update(self, *args, **kwargs):
        '''
        '''
        self.__init__(*args, **kwargs)