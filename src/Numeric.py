'''
@author Michael Duo Ling
@email duo.ling.cn@gmail.com
'''

from bitstring import BitArray
from typecheck import *
from Utilities import guarantee

class Numeric:
    pass

class Numeric:
    '''
    '''
    
    def __init__(self, *args, **kwargs):
        guarantee(False, "%s should not be instantiated." % __name__)
        
    @typecheck
    def _genBitString(self, size_in_bit: lambda x: x % 8 == 0, *args, **kwargs) -> BitArray:
        '''
        Generate a BitArray object and returns.

        @int=0 (int): initialize with an signed integer value.
        @uint=0 (int): initialize with an unsigned integer value.

        @return (BitArray): an instance of BitArray class.
        '''
        guarantee(len(args) == 0, "%s takes no positional args!" % __name__)
        result = BitArray(length=size_in_bit, uint=0)
        if len(kwargs.keys()) == 0:
            # no kwargs is given, use default value 0
            result.int = 0
        else:
            # handle kwargs
            guarantee(len(kwargs.keys()) == 1, "%s kwargs given, only 1 expected (int or uint)!" % len(args))
            guarantee(list(kwargs.keys())[0] in ('int', 'uint'),
                "%s is an invalid argument, only int or uint argument can be used!" % list(kwargs.keys())[0])
            if list(kwargs.keys())[0] == 'int':
                guarantee(kwargs['int'] >= -1 * (2 ** (size_in_bit - 1)) and kwargs['int'] <= (2 ** (size_in_bit - 1)) - 1,
                    "int(%d) is out of range!" % kwargs['int'])
                result.int = kwargs['int']
            else:
                guarantee(kwargs['uint'] >= 0 and kwargs['uint'] <= (2 ** size_in_bit) -1,
                    "uint(%d) is out of range!" % kwargs['uint'])
                result.uint = kwargs['uint']
        return result
    
    @typecheck
    def update(self, *args, **kwargs) -> nothing:
        '''
        Update the value of this Octa object. Note that parameter int and uint are exclusive.

        @int=0 (int): update with an signed integer value.
        @uint=0 (int): update with an unsigned integer value.

        @return (null)
        '''
        self.__init__(*args, **kwargs)
    
    @typecheck
    def __sub__(self, another: Numeric) -> Numeric:
        '''
        Two Numeric are subtracted as signed integer. Note that overflow would throw an exception.

        @another (Numeric): another Numeric instance.

        @return (Numeric): an instance of Numeric as result.
        '''
        #return Byte(int=(self._bitstring.int - another_byte._bitstring.int))
    
    @typecheck
    def __eq__(self, another: lambda x: isinstance(x, Numeric)) -> bool:
        '''
        Compare self with another object. Note that they have to have the same length!

        @another (Numeric): another Numeric instance.

        @return (bool): True if two Numeric are bit exact.
        
        @raise (MmixExcpetion): if two objects are not of same length
        '''
        return self.length == another.length and self._bitstring.uint == another._bitstring.uint