'''
Memory class.
'''
from Byte import Byte
from Wyde import Wyde
from Tetra import Tetra
from Octa import Octa
from typecheck import *
from Numeric import Range

class Memory:
    '''
    A class that simulates MMIX memory behaviour, which is implemented as a dictionary:
        address (uint) -> Byte
    '''
    def __init__(self):
        self.memory = dict()

    @typecheck
    def read(self, address: Octa, class_type: one_of((Byte, Wyde, Tetra, Octa))):
        '''
        Read memory by given address and data type.

        @address (Octa): memory address to start reading from (MSB)
        @class_type: Byte, Wyde, Tetra, or Octa

        @return: an object of requested class type.
        '''
        # address boundary check is done per __get_byte__ call.
        result = class_type()
        for offset in Range(Octa, 0, class_type.SIZE_IN_BYTE, 1):
            result.set_byte(offset.uint, self.__get_byte__(address + offset))
        return result

    @typecheck
    def set(self, address: Octa, class_type: one_of((Byte, Wyde, Tetra, Octa)), value):
        '''
        Set memory by given address and data type.

        @address (Octa): memory address to start setting from (MSB)
        @class_type: Byte, Wyde, Tetra, or Octa

        @return (None)
        '''
        # address boundary check is done per __set_byte__ call.
        if value.__class__ is not class_type:
            raise Exception("Given value is of class %s, but instance of class %s is expected." % (value.__class__, class_type))
        for offset in range(class_type.SIZE_IN_BYTE):
            tmp = value._bitstring[offset * Byte.SIZE_IN_BIT : offset * Byte.SIZE_IN_BIT + Byte.SIZE_IN_BIT].uint # pylint: disable=W0212
            self.__set_byte__(address.uint + offset, Byte(tmp))

    @typecheck
    def __get_byte__(self, address: Octa) -> Byte:
        '''
        Used internally to get an Byte object from given memory address. Return Byte(0x00) if that address is not found.
        '''
        # if address < 0 or address >= 2**64:
            # raise Exception("Memory_address={0:#0{width}} is out of boundary!".format(address, width=int(Octa.SIZE_IN_BIT / 4) + 2))
        if address.uint in self.memory:
            return Byte(self.memory[address.uint])
        return Byte()

    @typecheck
    def __set_byte__(self, address: int, byte: Byte) -> nothing:
        '''
        Used internally to store an Byte to given memory address.
        '''
        if address < 0 or address >= 2**64:
            raise Exception("Memory_address={0:#0{width}} is out of boundary!".format(address, width=int(Octa.SIZE_IN_BIT / 4) + 2))
        self.memory[address] = Byte(byte.uint)

    @typecheck
    def setByte(self, address: Octa, value: Byte) -> nothing:
        '''
        Store the given Byte to given address in memory.

        @address (Octa): address in memory to store the Byte;
        @value (Byte): Byte value to store.

        @return (None)
        '''
        self.set(address, Byte, value)

    @typecheck
    def readByte(self, address: Octa) -> Byte:
        '''
        Get an Byte object from given memory address.
        '''
        return self.read(address, Byte)

    @typecheck
    def setWyde(self, address: Octa, value: Wyde) -> nothing:
        '''
        Store the given Wyde to given address in memory.

        @address (Octa): address in memory to store the Byte;
        @value (Wyde): Wyde value to store.

        @return (None)
        '''
        self.set(address, Wyde, value)

    @typecheck
    def readWyde(self, address: Octa) -> Wyde:
        '''
        Get an Wyde object from given memory address.
        '''
        return self.read(address, Wyde)

    @typecheck
    def setTetra(self, address: Octa, value: Tetra) -> nothing:
        self.set(address, Tetra, value)

    @typecheck
    def readTetra(self, address: Octa) -> Tetra:
        return self.read(address, Tetra)

    @typecheck
    def setOcta(self, address, value):
        self.set(address, Octa, value)

    @typecheck
    def readOcta(self, address):
        return self.read(address, Octa)

    @typecheck
    def print_by_byte(self):
        '''
        A string representation of current values in memory. Uninitialized bytes in memory (set to 0 by default) will be omitted
        and printed as "...".

        @return (str): a string representation of memory.
        '''
        result = str()
        address_list = list(self.memory.keys())
        address_list.sort()
        is_first_entry = True
        previous_address_uint = -1
        for address_uint in address_list:
            if is_first_entry:
                is_first_entry = False
                if address_uint != 0:
                    result += "...\n"
                address = Octa(address_uint)
                result += "0x" + address.hex + ":\t0x" + self.readByte(address).hex + "\n"
            else:
                if address_uint != previous_address_uint+1:
                    result += "...\n"
                address = Octa(address_uint)
                result += "0x" + address.hex + ":\t0x" + self.readByte(address).hex + "\n"
            previous_address_uint = address_uint
        if address_list[-1] != 2**Octa.SIZE_IN_BIT-1:
            result += "...\n"
        return result

    @typecheck
    def print_by_wyde(self):
        '''
        A string representation of current values in memory. Uninitialized wydes in memory (set to 0 by default) will be omitted
        and printed as "...".

        @return (str): a string representation of memory.
        '''
        result = str()
        address_list = list(self.memory.keys())
        #print("\n===DEBUG===\n")
        #print("address_list=%s" % address_list)
        #print("\n===DEBUG===\n")
        address_list.sort()
        #print("\n===DEBUG===\n")
        #print("address_list=%s" % address_list)
        #print("\n===DEBUG===\n")
        is_first_entry = True
        previous_address_uint = -1 * Wyde.SIZE_IN_BYTE
        for address_uint in address_list:
            #print("\n===DEBUG===\n")
            #print("address_uint=%s" % hex(address_uint))
            #print("\n===DEBUG===\n")
            if is_first_entry:
                is_first_entry = False
                if address_uint >= Wyde.SIZE_IN_BYTE:
                    # the first Wyde won't be printed
                    result += "...\n"
            if address_uint < previous_address_uint + Wyde.SIZE_IN_BYTE:
                # this byte is already printed
                continue
            else:
                # we need to print this Wyde
                # align to Wyde boundary
                address_uint -= address_uint % Wyde.SIZE_IN_BYTE
                #print("\n===DEBUG===\n")
                #print("after aligning address_uint=%s" % hex(address_uint))
                #print("\n===DEBUG===\n")
                if address_uint != previous_address_uint+Wyde.SIZE_IN_BYTE:
                    result += "...\n"
            address = Octa(address_uint)
            result += "0x" + address.hex + ":\t0x" + self.readWyde(address).hex + "\n"
            previous_address_uint = address_uint
        if address_list[-1] != 2**Octa.SIZE_IN_BIT-Wyde.SIZE_IN_BYTE:
            result += "...\n"
        return result
