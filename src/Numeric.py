'''
@author Michael Duo Ling
@email duo.ling.cn@gmail.com
'''

from bitstring import BitArray
from typecheck import *
from Utilities import guarantee

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
            guarantee(
                list(kwargs.keys())[0] in ('int', 'uint'),
                "%s is an invalid argument, only int or uint argument can be used!" % list(kwargs.keys())[0]
                )
            if list(kwargs.keys())[0] == 'int':
                guarantee(
                    kwargs['int'] >= -1 * (2 ** (size_in_bit - 1)) and kwargs['int'] <= (2 ** (size_in_bit - 1)) - 1,
                    "int(%d) is out of range!" % kwargs['int']
                    )
                result.int = kwargs['int']
            else:
                guarantee(
                    kwargs['uint'] >= 0 and kwargs['uint'] <= (2 ** size_in_bit) -1,
                    "uint(%d) is out of range!" % kwargs['uint']
                    )
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
    def __and__(self, another: lambda x: isinstance(x, Numeric)) -> lambda x: isinstance(x, Numeric):
        '''
        Bit and operator (&).

        @another (Numeric): another Numeric instance.

        @return (Numeric): an instance of Numeric as bit and result.
        '''
        return self.__class__(uint=(self._bitstring & another._bitstring).uint)

    @typecheck
    def __or__(self, another: lambda x: isinstance(x, Numeric)) -> lambda x: isinstance(x, Numeric):
        '''
        Bit or operator (|).

        @another (Numeric): another Numeric instance.

        @return (Numeric): an instance of Numeric as bit or result.
        '''
        return self.__class__(uint=(self._bitstring | another._bitstring).uint)

    @typecheck
    def __xor__(self, another: lambda x: isinstance(x, Numeric)) -> lambda x: isinstance(x, Numeric):
        '''
        Bit xor operator (^).

        @another (Numeric): another Numeric instance.

        @return (Numeric): an instance of Numeric as bit xor result.
        '''
        return self.__class__(uint=(self._bitstring ^ another._bitstring).uint)

    @typecheck
    def __add__(self, another: lambda x: isinstance(x, Numeric)) -> lambda x: isinstance(x, Numeric):
        '''
        Two Numeric are added as signed integer. Note that overflow would throw and exception.

        @another (Numeric): another Numeric instance.

        @return (Numeric): an instance of Numeric as result self+another.
        '''
        return self.__class__(int=(self._bitstring.int + another._bitstring.int))

    @typecheck
    def __sub__(self, another: lambda x: isinstance(x, Numeric)) -> lambda x: isinstance(x, Numeric):
        '''
        Two Numeric are subtracted as signed integer. Note that overflow would throw an exception.

        @another (Numeric): another Numeric instance.

        @return (Numeric): an instance of Numeric as result.
        '''
        guarantee(self.length == another.length, "Numeric with different length cannot be subtracted!")
        return self.__class__(int=(self._bitstring.int - another._bitstring.int))

    @typecheck
    def __eq__(self, another: lambda x: isinstance(x, Numeric)) -> bool:
        '''
        Compare self with another object. Note that they have to have the same length!

        @another (Numeric): another Numeric instance.

        @return (bool): True if two Numeric are bit exact.

        @raise (MmixExcpetion): if two objects are not of same length
        '''
        guarantee(self.length == another.length, "Numeric with different length cannot be compared!")
        return self.length == another.length and self._bitstring.uint == another._bitstring.uint

    @typecheck
    def __repr__(self) -> str:
        '''
        Override default to give a hex representation of this number, formatted according to its length.
        '''
        return '{0:#0{width}x}'.format(self.uint, width=int(self.length / 4) + 2)
