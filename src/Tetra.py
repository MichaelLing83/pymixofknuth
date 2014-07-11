'''
Author: Michael Duo Ling
'''
from typecheck import *
from Numeric import Numeric

class Tetra(Numeric):
    '''
    work-around to refer to Tetra in typecheck
    '''
    pass

class Tetra(Numeric):
    '''
    4 Bytes numeric.
    '''

    SIZE_IN_BYTE = 4    # 4 Byte
    SIZE_IN_BIT = SIZE_IN_BYTE * Numeric.BYTE_SIZE_IN_BIT   # bits

    @typecheck
    def __init__(   #pylint: disable=W0231
            self,
            value: lambda x: isinstance(x, Tetra) or isinstance(x, int)=0
        ) -> nothing:
        '''
        Create a Tetra object.

        @return (Tetra): an instance of Tetra class.
        '''
        self.__init_self__(Tetra, value)
