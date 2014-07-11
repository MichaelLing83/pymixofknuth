'''
@author Michael Duo Ling
@email duo.ling.cn@gmail.com
'''

from bitstring import BitArray
from typecheck import *
from Utilities import guarantee
from copy import deepcopy

class Numeric:  # pylint: disable=W0232,R0903
    '''
    work-around to refer to Numeric in typecheck
    '''
    pass

class Numeric:  # pylint: disable=E0102
    '''
    Base class for all numeric classes, e.g. Byte, Wyde, Tetra, Octa.
    '''
    BYTE_SIZE_IN_BIT = 8

    def __init__(self, *args, **kwargs):    # pylint: disable=W0613
        '''
        Numeric should never be instantiated.
        '''
        guarantee(False, "%s should not be instantiated." % __name__)

    @typecheck
    def __init_self__(
            self,
            klass: with_attr("SIZE_IN_BIT"),
            value: lambda x: isinstance(x, Numeric) or isinstance(x, int)=0
        ) -> nothing:
        '''
        Used internally to initialize numeric instances. So all subclasses share this generic method, and Numeric doesn't have to know
        about its subclasses.

        @klass: a subclass of Numeric
        @value: value used to initialize

        @return (None)
        '''
        if isinstance(value, Numeric):
            # copy construction
            self._bitstring = deepcopy(value._bitstring)    # pylint: disable=W0212,E1103
        else:
            # init with an integer
            if value < 0:
                self._bitstring = self._genBitString(klass.SIZE_IN_BIT, int=value)
            else:
                self._bitstring = self._genBitString(klass.SIZE_IN_BIT, uint=value)
        self.length = self._bitstring.length
        self.int = self._bitstring.int
        self.uint = self._bitstring.uint
        self.bin = self._bitstring.bin
        self.hex = self._bitstring.hex

    @typecheck
    def _genBitString(self, size_in_bit: lambda x: x % Numeric.BYTE_SIZE_IN_BIT == 0, *args, **kwargs) -> BitArray:
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
                    "int(%d) is out of range for %d bits!" % (kwargs['int'], size_in_bit)
                    )
                result.int = kwargs['int']
            else:
                guarantee(
                    kwargs['uint'] >= 0 and kwargs['uint'] <= (2 ** size_in_bit) -1,
                    "uint(%d) is out of range for %d bits!" % (kwargs['uint'], size_in_bit)
                    )
                result.uint = kwargs['uint']
        return result

    @typecheck
    def set_value(
            self,
            value: lambda x: isinstance(x, Numeric) or isinstance(x, int)=0
        ) -> nothing:
        '''
        Update the value of this Octa object. Note that parameter int and uint are exclusive.

        @return (null)
        '''
        self.__init_self__(self.__class__, value)

    @typecheck
    def set_byte(
            self,
            index: lambda x: isinstance(x, Numeric) or isinstance(x, int),
            value: lambda x: isinstance(x, Numeric) and x.__class__.SIZE_IN_BYTE == 1
        ) -> nothing:
        '''
        Set given byte with value. Note that index is counted from MSB!
        '''
        if isinstance(index, Numeric):
            index = index.uint
        guarantee(
            index >= 0 and index < self.__class__.SIZE_IN_BYTE, # pylint: disable=E1101
            "Given index={index} is out of range for class {klass}!".format(index=index, klass=self.__class__)
            )
        mask = 2 ** self.__class__.SIZE_IN_BIT - 1 # pylint: disable=E1101
        mask = mask ^ (0xff << ((self.__class__.SIZE_IN_BYTE - index - 1) * Numeric.BYTE_SIZE_IN_BIT))  # mask off the correct byte
        tmp = self.uint & mask  # mask off the byte to set in this object
        tmp = tmp | value.uint << ((self.__class__.SIZE_IN_BYTE - index - 1) * Numeric.BYTE_SIZE_IN_BIT)
        self.__init_self__(self.__class__, tmp)

    @typecheck
    def slice(
            self,
            index: lambda x: isinstance(x, Numeric) or isinstance(x, int),
            klass: lambda x: issubclass(x, Numeric)
        ) -> lambda x: isinstance(x, Numeric):
        '''
        Slice numeric as an Byte array, starting from index (counted from MSB) and take a piece that's length of given class.

        E.g.
            Byte(0x12).slice(0, Byte)   # Byte(0x12)
            Wyde(0x1234).slice(1, Byte) # Byte(0x34)
            Tetra(0x12345678).slice(1, Wyde)    # Wyde(0x3456)
        '''
        if isinstance(index, Numeric):
            index = index.uint
        guarantee(
            index >= 0 and index + klass.SIZE_IN_BYTE - 1 < self.__class__.SIZE_IN_BYTE,
            "Given index={index}, class={klass} is out of range for class {this_klass}!".format(
                index=index, klass=klass, this_klass=self.__class__
                )
            )
        mask = (2 ** klass.SIZE_IN_BIT - 1) << ((self.__class__.SIZE_IN_BYTE - index - klass.SIZE_IN_BYTE) * Numeric.BYTE_SIZE_IN_BIT)
        tmp = self.uint & mask  # mask to have only the bytes to get in this object
        tmp = tmp >> ((self.__class__.SIZE_IN_BYTE - index - klass.SIZE_IN_BYTE) * Numeric.BYTE_SIZE_IN_BIT)
        return klass(tmp)

    @typecheck
    def update(
            self,
            index: lambda x: isinstance(x, Numeric) or isinstance(x, int),
            value: lambda x: isinstance(x, Numeric)
        ) -> lambda x: isinstance(x, Numeric):
        '''
        Update numeric as an Byte array, starting from index (counted from MSB) and update a piece (or all) that's length of given value.
        Note it updates in-place (mutable change) and also return the instance self.

        E.g.
            Byte(0x12).update(0, Byte(0x34))   # Byte(0x34)
            Wyde(0x1234).update(1, Byte(0x12)) # Wyde(0x1212)
            Tetra(0x12345678).update(1, Wyde(0x0987))    # Tetra(0x12098778)
        '''
        if isinstance(index, Numeric):
            index = index.uint
        guarantee(
            index >= 0 and index + value.__class__.SIZE_IN_BYTE - 1 < self.__class__.SIZE_IN_BYTE,
            "Given index={index}, class={klass} is out of range for class {this_klass}!".format(
                index=index, klass=value.__class__, this_klass=self.__class__
                )
            )
        mask = (2 ** value.__class__.SIZE_IN_BIT - 1) << (
            (self.__class__.SIZE_IN_BYTE - index - value.__class__.SIZE_IN_BYTE) * Numeric.BYTE_SIZE_IN_BIT
            )
        tmp = self.uint & (~mask)  # mask away the bytes to update in this object
        tmp = tmp | (value.uint << ((self.__class__.SIZE_IN_BYTE - index - value.__class__.SIZE_IN_BYTE) * Numeric.BYTE_SIZE_IN_BIT))
        self.__init_self__(self.__class__, tmp)
        return self

    @typecheck
    def __and__(self, another: lambda x: isinstance(x, Numeric)) -> lambda x: isinstance(x, Numeric):
        '''
        Bit and operator (&).

        @another (Numeric): another Numeric instance.

        @return (Numeric): an instance of Numeric as bit and result.
        '''
        return self.__class__((self._bitstring & another._bitstring).uint)

    @typecheck
    def __or__(self, another: lambda x: isinstance(x, Numeric)) -> lambda x: isinstance(x, Numeric):
        '''
        Bit or operator (|).

        @another (Numeric): another Numeric instance.

        @return (Numeric): an instance of Numeric as bit or result.
        '''
        return self.__class__((self._bitstring | another._bitstring).uint)

    @typecheck
    def __xor__(self, another: lambda x: isinstance(x, Numeric)) -> lambda x: isinstance(x, Numeric):
        '''
        Bit xor operator (^).

        @another (Numeric): another Numeric instance.

        @return (Numeric): an instance of Numeric as bit xor result.
        '''
        return self.__class__((self._bitstring ^ another._bitstring).uint)

    @typecheck
    def __add__(self, another: lambda x: isinstance(x, Numeric)) -> lambda x: isinstance(x, Numeric):
        '''
        Two Numeric are added as signed integer. Note that overflow would throw and exception.

        @another (Numeric): another Numeric instance.

        @return (Numeric): an instance of Numeric as result self+another.
        '''
        return self.__class__(self._bitstring.int + another._bitstring.int)

    @typecheck
    def __sub__(self, another: lambda x: isinstance(x, Numeric)) -> lambda x: isinstance(x, Numeric):
        '''
        Two Numeric are subtracted as signed integer. Note that overflow would throw an exception.

        @another (Numeric): another Numeric instance.

        @return (Numeric): an instance of Numeric as result.
        '''
        guarantee(self.length == another.length, "Numeric with different length cannot be subtracted!")
        return self.__class__(self._bitstring.int - another._bitstring.int)

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
    def __lshift__(self, other: int) -> lambda x: isinstance(x, Numeric):
        '''
        '''
        tmp = deepcopy(self._bitstring)
        tmp <<= other
        return self.__class__(tmp.uint)

    @typecheck
    def __repr__(self) -> str:
        '''
        Override default to give a hex representation of this number, formatted according to its length.
        '''
        return '{0:#0{width}x}'.format(self.uint, width=int(self.length / 4) + 2)

class Range:
    '''
    Iterator that yields numeric objects based of given class and range.
    '''
    @typecheck
    def __init__(
            self,
            klass: lambda x: issubclass(x, Numeric),
            start: lambda x: isinstance(x, Numeric) or isinstance(x, int),
            end: lambda x: isinstance(x, Numeric) or isinstance(x, int),
            step: lambda x: isinstance(x, Numeric) or isinstance(x, int),
        ):
        '''
        Create an iterator that yields give class of objects.
        '''
        self.klass = klass
        if isinstance(start, Numeric):
            self.start = start.int
        else:
            self.start = start
        if isinstance(end, Numeric):
            self.end = end.int
        else:
            self.end = end
        if isinstance(step, Numeric):
            self.step = step.int
        else:
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        obj = self.klass(self.start)
        self.start += self.step
        return obj
