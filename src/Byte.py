'''
@author Michael Duo Ling
@email duo.ling.cn@gmail.com

A class representing one byte (i.e. 8 bit).
'''

from bitstring import BitArray

class Byte:
    '''
    One byte = 8 bits.
    '''
    SIZE_IN_BIT = 8
    def __init__(self, int=0, uint=0):
        '''
        Initializer. Note that parameter int and uint are exclusive.

        @int=0 (int): initialize with an signed integer value.
        @uint=0 (int): initialize with an unsigned integer value.

        @return (Byte): an instance of Byte class.
        '''
        self.byte = BitArray(length=Byte.SIZE_IN_BIT, uint=0)
        self.length = self.byte.length
        if int!=0 and uint==0:
            self.byte.int = int
        elif int==0 and uint!=0:
            self.byte.uint = uint
        self.int = self.byte.int
        self.uint = self.byte.uint
        self.bin = self.byte.bin
        self.hex = self.byte.hex
    
    def __and__(self, another_byte):
        '''
        Bit and operator (&).

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as bit and result.
        '''
        return Byte(uint=(self.byte & another_byte.byte).uint)
    
    def __or__(self, another_byte):
        '''
        Bit or operator (|).

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as bit or result.
        '''
        return Byte(uint=(self.byte | another_byte.byte).uint)
    
    def __xor__(self, another_byte):
        '''
        Bit xor operator (^).

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as bit xor result.
        '''
        return Byte(uint=(self.byte ^ another_byte.byte).uint)
    
    def __add__(self, another_byte):
        '''
        Two Byte are added as signed integer. Note that overflow would throw and exception.

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as result self+another_byte.
        '''
        return Byte(int=(self.byte.int + another_byte.byte.int))
    
    def __sub__(self, another_byte):
        '''
        Two Byte are subtracted as signed integer. Note that overflow would throw and exception.

        @another_byte (Byte): another Byte instance.

        @return (Byte): an instance of Byte as result self-another_byte.
        '''
        return Byte(int=(self.byte.int - another_byte.byte.int))
    
    def __eq__(self, another_byte):
        '''
        Compare self with another_byte.

        @another_byte (Byte): another Byte instance.

        @return (bool): True if two Bytes are bit exact.
        '''
        return self.byte.uint == another_byte.byte.uint
    
    def update(self, int=0, uint=0):
        '''
        Update the value of this Byte object. Note that parameter int and uint are exclusive.

        @int=0 (int): update with an signed integer value.
        @uint=0 (int): update with an unsigned integer value.

        @return (null)
        '''
        if int!=0 and uint==0:
            self.byte.int = int
        elif int==0 and uint!=0:
            self.byte.uint = uint
        else:
            self.byte.int = 0
        self.int = self.byte.int
        self.uint = self.byte.uint
        self.bin = self.byte.bin
        self.hex = self.byte.hex