'''
Author: Michael Duo Ling
'''
from typecheck import *
from Numeric import Numeric

class Wyde(Numeric):
    '''
    work-around to refer to Wyde in typecheck
    '''
    pass

class Wyde(Numeric):
    '''
    2 Bytes numeric.
    '''

    SIZE_IN_BYTE = 2    # 2 Byte
    SIZE_IN_BIT = SIZE_IN_BYTE * Numeric.BYTE_SIZE_IN_BIT   # bits

    @typecheck
    def __init__(   # pylint: disable=W0231
            self,
            value: lambda x: isinstance(x, Wyde) or isinstance(x, int)=0
        ) -> nothing:
        '''
        Create a Wyde object.

        @return (Wyde): an instance of Wyde class.
        '''
        self.__init_self__(Wyde, value)
