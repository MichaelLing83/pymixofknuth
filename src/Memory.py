from Byte import Byte
from Wyde import Wyde
from Tetra import Tetra
from Octa import Octa
from typecheck import *

class Memory:
    '''
    A class that simulates MMIX memory behaviour, which is implemented as a dictionary:
        address (uint) -> Byte
    '''
    def __init__(self):
        self.memory = dict()

    @typecheck
    def __get_byte__(self, address: int) -> Byte:
        '''
        Used internally to get an Byte object from given memory address. Return Byte(uint=0x00) if that address is not found.
        '''
        if address < 0 or address >= 2**64:
            raise Exception("Memory_address={0:#0{width}} is out of boundary!".format(address, width=int(Octa.SIZE_IN_BIT / 4) + 2))
        if address in self.memory:
            return Byte(uint=self.memory[address].uint)
        return Byte(uint=0x00)

    @typecheck
    def __set_byte__(self, address: int, byte: Byte) -> nothing:
        '''
        Used internally to store an Byte to given memory address.
        '''
        if address < 0 or address >= 2**64:
            raise Exception("Memory_address={0:#0{width}} is out of boundary!".format(address, width=int(Octa.SIZE_IN_BIT / 4) + 2))
        self.memory[address] = Byte(uint=byte.uint)

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
        # if address.uint >= 2**64:
            # raise Exception("Memory_address=%s is out of boundary!" % address.hex)
        # result = 0
        # if address.uint in self.memory:
            # result = self.memory[address.uint].uint << 8
        # if address.uint+1 in self.memory:
            # result += self.memory[address.uint+1].uint
        # # return '0x0000' by default
        # return Wyde(uint=result)

    @typecheck
    def setTetra(self, address, value):
        if address.uint >= 2**64:
            raise Exception("Memory_address=%s is out of boundary!" % address.hex)
        byte_mask = 0b11111111
        size_in_byte = int(Tetra.SIZE_IN_BIT/Byte.SIZE_IN_BIT)
        #print("size_in_byte=", size_in_byte)
        for offset in range(size_in_byte):
            if address.uint+offset in self.memory:
                # mask to keep only the relevant byte
                tmp = value.uint & (byte_mask<<((size_in_byte-offset)*8))
                #print("Input value 0x", value.hex)
                #print((value.uint&(byte_mask<<((size_in_byte-offset)*8)))>>((size_in_byte-offset)*8))
                tmp >>= (size_in_byte-1-offset)*8
                #print("tmp shifted 0x", Wyde(uint=tmp).hex)
                self.memory[address.uint+offset] = Byte(uint=tmp)
            else:
                # mask to keep only the relevant byte
                tmp = value.uint & (byte_mask<<((size_in_byte-1-offset)*8))
                #print("Input value 0x", value.hex)
                #print("tmp         0x", Wyde(uint=tmp).hex)
                tmp >>= (size_in_byte-1-offset)*8
                #print("tmp shifted 0x", Wyde(uint=tmp).hex)
                self.memory[address.uint+offset] = Byte(uint=tmp)

    @typecheck
    def readTetra(self, address):
        if address.uint >= 2**64:
            raise Exception("Memory_address=%s is out of boundary!" % address.hex)
        result = 0
        size_in_byte = int(Tetra.SIZE_IN_BIT/Byte.SIZE_IN_BIT)
        for offset in range(size_in_byte):
            if address.uint in self.memory:
                result += self.memory[address.uint+offset].uint << (8*(size_in_byte-offset-1))
        # return '0x0000' by default
        return Tetra(uint=result)

    @typecheck
    def set(self, address, classType, value):
        if address.uint >= 2**64:
            raise Exception("Memory_address=%s is out of boundary!" % address.hex)
        if value.__class__ is not classType:
            raise Exception("Given value is of class %s, but instance of class %s is expected." % (value.__class__, classType))
        byte_mask = 0b11111111
        size_in_byte = int(classType.SIZE_IN_BIT/Byte.SIZE_IN_BIT)
        #print("size_in_byte=", size_in_byte)
        for offset in range(size_in_byte):
            if address.uint+offset in self.memory:
                # mask to keep only the relevant byte
                tmp = value.uint & (byte_mask<<((size_in_byte-offset)*8))
                #print("Input value 0x", value.hex)
                #print((value.uint&(byte_mask<<((size_in_byte-offset)*8)))>>((size_in_byte-offset)*8))
                tmp >>= (size_in_byte-1-offset)*8
                #print("tmp shifted 0x", Wyde(uint=tmp).hex)
                self.memory[address.uint+offset] = Byte(uint=tmp)
            else:
                # mask to keep only the relevant byte
                tmp = value.uint & (byte_mask<<((size_in_byte-1-offset)*8))
                #print("Input value 0x", value.hex)
                #print("tmp         0x", Wyde(uint=tmp).hex)
                tmp >>= (size_in_byte-1-offset)*8
                #print("tmp shifted 0x", Wyde(uint=tmp).hex)
                self.memory[address.uint+offset] = Byte(uint=tmp)

    @typecheck
    def read(self, address, classType):
        if address.uint + classType.SIZE_IN_BYTE -1 >= 2**64:
            raise Exception("Memory_address=%s is out of boundary!" % address.hex)
        result = 0
        size_in_byte = int(classType.SIZE_IN_BIT / Byte.SIZE_IN_BIT)
        for offset in range(size_in_byte):
            result += self.__get_byte__(address.uint + offset).uint << (8*(size_in_byte-offset-1))
            # if address.uint in self.memory:
                # result += self.memory[address.uint+offset].uint << (8*(size_in_byte-offset-1))
        # return '0x0000' by default
        return classType(uint=result)

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
                address = Octa(uint=address_uint)
                result += "0x" + address.hex + ":\t0x" + self.readByte(address).hex + "\n"
            else:
                if address_uint != previous_address_uint+1:
                    result += "...\n"
                address = Octa(uint=address_uint)
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
            address = Octa(uint=address_uint)
            result += "0x" + address.hex + ":\t0x" + self.readWyde(address).hex + "\n"
            previous_address_uint = address_uint
        if address_list[-1] != 2**Octa.SIZE_IN_BIT-Wyde.SIZE_IN_BYTE:
            result += "...\n"
        return result
