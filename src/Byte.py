'''
@author Michael Duo Ling
@email duo.ling.cn@gmail.com

A class representing one byte (i.e. 8 bit).
'''

from bitstring import BitArray
from typecheck import *
from Utilities import guarantee
from Numeric import Numeric

class Byte(Numeric):
    # TODO: is this work-around necessary to refer to Byte in its class definition?
    pass

class Byte(Numeric):
    '''
    One byte = 8 bits.
    '''
    SIZE_IN_BIT = 8
    
    @typecheck
    def __init__(self, *args, **kwargs) -> nothing:
        '''
        Initializer. Note that parameter int and uint are exclusive.

        @int=0 (int): initialize with an signed integer value.
        @uint=0 (int): initialize with an unsigned integer value.

        @return (Byte): an instance of Byte class.
        '''
        self._bitstring = self._genBitString(Byte.SIZE_IN_BIT, *args, **kwargs)
        self.length = self._bitstring.length
        self.int = self._bitstring.int
        self.uint = self._bitstring.uint
        self.bin = self._bitstring.bin
        self.hex = self._bitstring.hex
    
    def __and__(self, another_byte: Byte) -> Byte:
        '''
        Bit and operator (&).

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as bit and result.
        '''
        return Byte(uint=(self._bitstring & another_byte._bitstring).uint)
    
    def __or__(self, another_byte: Byte) -> Byte:
        '''
        Bit or operator (|).

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as bit or result.
        '''
        return Byte(uint=(self._bitstring | another_byte._bitstring).uint)
    
    def __xor__(self, another_byte: Byte) -> Byte:
        '''
        Bit xor operator (^).

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as bit xor result.
        '''
        return Byte(uint=(self._bitstring ^ another_byte._bitstring).uint)
    
    def __add__(self, another_byte: Byte) -> Byte:
        '''
        Two Byte are added as signed integer. Note that overflow would throw and exception.

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as result self+another_byte.
        '''
        return Byte(int=(self._bitstring.int + another_byte._bitstring.int))
    
    def __sub__(self, another_byte: Byte) -> Byte:
        '''
        Two Byte are subtracted as signed integer. Note that overflow would throw and exception.

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as result self-another_byte.
        '''
        return Byte(int=(self._bitstring.int - another_byte._bitstring.int))
