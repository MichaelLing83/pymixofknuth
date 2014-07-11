'''
@author Michael Duo Ling
@email duo.ling.cn@gmail.com

A class representing one byte (i.e. 8 bit).
'''

from typecheck import *
from Numeric import Numeric

class Byte(Numeric):
    # work-around to refer to Byte in typecheck
    pass

class Byte(Numeric):
    '''
    One byte = 8 bits.
    '''
    SIZE_IN_BIT = Numeric.BYTE_SIZE_IN_BIT
    SIZE_IN_BYTE = 1

    @typecheck
    def __init__(
            self,
            value: lambda x: isinstance(x, Byte) or isinstance(x, int)=0
        ) -> nothing:
        '''
        Create a Byte object.

        @return (Byte): an instance of Byte class.
        '''
        self.__init_self__(Byte, value)
