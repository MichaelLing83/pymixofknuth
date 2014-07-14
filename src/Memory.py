'''
Memory class.
'''
from Numeric import Numeric #pylint: disable=W0611
from Byte import Byte
from Wyde import Wyde   #pylint: disable=W0611
from Tetra import Tetra # pylint: disable=W0611
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
        # address boundary check is implied by Octa object
        result = class_type()
        for offset in Range(Octa, 0, class_type.SIZE_IN_BYTE, 1):
            result.set_byte(offset, self.memory.get((address + offset).uint, Byte(0)))
        return result

    @typecheck
    def set(self, address: Octa, value: Numeric) -> nothing:
        '''
        Set memory by given address and data type.

        @address (Octa): memory address to start setting from (MSB)

        @return (None)
        '''
        # address boundary check is implied by Octa object
        for offset in Range(Octa, 0, value.__class__.SIZE_IN_BYTE, 1):
            self.memory[(address + offset).uint] = value.slice(offset, Byte)

    @typecheck
    def to_str(
            self,
            klass: lambda x: issubclass(x, Numeric)
        ) -> str:
        '''
        Return a string representation of Memory class instance.
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
        previous_address_uint = -1 * klass.SIZE_IN_BYTE
        for address_uint in address_list:
            #print("\n===DEBUG===\n")
            #print("address_uint=%s" % hex(address_uint))
            #print("\n===DEBUG===\n")
            if is_first_entry:
                is_first_entry = False
                if address_uint >= klass.SIZE_IN_BYTE:
                    # the first klass won't be printed
                    result += "...\n"
                    previous_address_uint = 0
            if address_uint < previous_address_uint + klass.SIZE_IN_BYTE:
                # this byte is already printed
                continue
            else:
                # we need to print this klass
                # align to klass boundary
                address_uint -= address_uint % klass.SIZE_IN_BYTE
                #print("\n===DEBUG===\n")
                #print("after aligning address_uint=%s" % hex(address_uint))
                #print("\n===DEBUG===\n")
                if address_uint != previous_address_uint + klass.SIZE_IN_BYTE:
                    result += "...\n"
            address = Octa(address_uint)
            result += "0x" + address.hex + ":\t0x" + self.read(address, klass).hex + "\n"
            previous_address_uint = address_uint
        if address_list[-1] != 2 ** Octa.SIZE_IN_BIT - klass.SIZE_IN_BYTE:
            result += "...\n"
        return result
