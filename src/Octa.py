'''
Author: Michael Duo Ling
'''
from Numeric import Numeric
from typecheck import *

class Octa(Numeric):
    '''
    work-around to refer to Octa in typecheck
    '''
    pass

class Octa(Numeric):
    '''
    8 Byte numeric class.
    '''

    SIZE_IN_BYTE = 8    # 8 Byte
    SIZE_IN_BIT = SIZE_IN_BYTE * Numeric.BYTE_SIZE_IN_BIT   # bits

    @typecheck
    def __init__(   # pylint: disable=W0231
            self,
            value: lambda x: isinstance(x, Octa) or isinstance(x, int)=0
        ) -> nothing:
        '''
        Create a Octa object.

        @return (Octa): an instance of Octa class.
        '''
        self.__init_self__(Octa, value)
