'''
@author Michael Duo Ling
@email duo.ling.cn@gmail.com

A class representing one byte (i.e. 8 bit).
'''

from bitstring import BitArray
from typecheck import *
from Utilities import guarantee

class Byte:
    # TODO: is this work-around necessary to refer to Byte in its class definition?
    pass

class Byte:
    '''
    One byte = 8 bits.
    '''
    SIZE_IN_BIT = 8
    __MIN_BYTE_INT = -1 * (2 ** (8 - 1))
    __MAX_BYTE_INT = (2 ** (8 - 1)) - 1
    __MIN_BYTE_UINT = 0
    __MAX_BYTE_UINT = (2 ** 8) -1
    
    @typecheck
    #def __init__(self, int: __byte_int=0, uint: __byte_uint=0)-> nothing:
    def __init__(self, *args, **kwargs) -> nothing:
        '''
        Initializer. Note that parameter int and uint are exclusive.

        @int=0 (int): initialize with an signed integer value.
        @uint=0 (int): initialize with an unsigned integer value.

        @return (Byte): an instance of Byte class.
        '''
        guarantee(len(args) == 0, "no positional args allowed")
        self.byte = BitArray(length=Byte.SIZE_IN_BIT, uint=0)
        self.length = self.byte.length
        if len(kwargs.keys()) == 0:
            # no kwargs is given, use default value 0
            self.byte.int = 0
        else:
            # handle kwargs
            guarantee(len(kwargs.keys()) == 1, "%s kwargs given, only 1 expected (int or uint)!" % len(args))
            guarantee(list(kwargs.keys())[0] in ('int', 'uint'),
                "%s is an invalid argument, only int or uint argument can be used!" % list(kwargs.keys())[0])
            if list(kwargs.keys())[0] == 'int':
                guarantee(kwargs['int'] >= Byte.__MIN_BYTE_INT and kwargs['int'] <= Byte.__MAX_BYTE_INT,
                    "int(%d) is out of range for Byte!" % kwargs['int'])
                self.byte.int = kwargs['int']
            else:
                guarantee(kwargs['uint'] >= Byte.__MIN_BYTE_UINT and kwargs['uint'] <= Byte.__MAX_BYTE_UINT,
                    "uint(%d) is out of range for Byte!" % kwargs['uint'])
                self.byte.uint = kwargs['uint']
        self.int = self.byte.int
        self.uint = self.byte.uint
        self.bin = self.byte.bin
        self.hex = self.byte.hex
    
    def __and__(self, another_byte: Byte) -> Byte:
        '''
        Bit and operator (&).

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as bit and result.
        '''
        return Byte(uint=(self.byte & another_byte.byte).uint)
    
    def __or__(self, another_byte: Byte) -> Byte:
        '''
        Bit or operator (|).

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as bit or result.
        '''
        return Byte(uint=(self.byte | another_byte.byte).uint)
    
    def __xor__(self, another_byte: Byte) -> Byte:
        '''
        Bit xor operator (^).

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as bit xor result.
        '''
        return Byte(uint=(self.byte ^ another_byte.byte).uint)
    
    def __add__(self, another_byte: Byte) -> Byte:
        '''
        Two Byte are added as signed integer. Note that overflow would throw and exception.

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as result self+another_byte.
        '''
        return Byte(int=(self.byte.int + another_byte.byte.int))
    
    def __sub__(self, another_byte: Byte) -> Byte:
        '''
        Two Byte are subtracted as signed integer. Note that overflow would throw and exception.

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as result self-another_byte.
        '''
        return Byte(int=(self.byte.int - another_byte.byte.int))
    
    def __eq__(self, another_byte: Byte) -> Byte:
        '''
        Compare self with another_byte.

        @another_byte (Byte): another Byte instance.

        @return (bool): True if two Bytes are bit exact.
        '''
        return self.byte.uint == another_byte.byte.uint
    
    def update(self, *args, **kwargs) -> nothing:
        '''
        Update the value of this Byte object. Note that parameter int and uint are exclusive.

        @int=0 (int): update with an signed integer value.
        @uint=0 (int): update with an unsigned integer value.

        @return (null)
        '''
        self.__init__(*args, **kwargs)
        return