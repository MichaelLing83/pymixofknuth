﻿from Byte import Byte
from Wyde import Wyde
from Tetra import Tetra
from Octa import Octa

class Memory:
    def __init__(self):
        self.memory = dict()
    
    def setByte(self, address, value):
        if address.uint >= 2**64:
            raise Exception("Memory_address=%s is out of boundary!" % address.hex)
        if address.uint in self.memory:
            self.memory[address.uint].update(uint=value.uint)
        else:
            self.memory[address.uint] = Byte(uint=value.uint)
    
    def readByte(self, address):
        if address.uint >= 2**64:
            raise Exception("Memory_address=%s is out of boundary!" % address.hex)
        if address.uint in self.memory:
            return Byte(uint=self.memory[address.uint].uint)
        # return '0x00' by default
        return Byte()
    
    def setWyde(self, address, value):
        if address.uint >= 2**64:
            raise Exception("Memory_address=%s is out of boundary!" % address.hex)
        byte_mask = 0b11111111
        size_in_byte = int(Wyde.SIZE_IN_BIT/Byte.SIZE_IN_BIT)
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
    
    def readWyde(self, address):
        if address.uint >= 2**64:
            raise Exception("Memory_address=%s is out of boundary!" % address.hex)
        result = 0
        if address.uint in self.memory:
            result = self.memory[address.uint].uint << 8
        if address.uint+1 in self.memory:
            result += self.memory[address.uint+1].uint
        # return '0x0000' by default
        return Wyde(uint=result)
    
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
    
    def read(self, address, classType):
        if address.uint >= 2**64:
            raise Exception("Memory_address=%s is out of boundary!" % address.hex)
        result = 0
        size_in_byte = int(classType.SIZE_IN_BIT/Byte.SIZE_IN_BIT)
        for offset in range(size_in_byte):
            if address.uint in self.memory:
                result += self.memory[address.uint+offset].uint << (8*(size_in_byte-offset-1))
        # return '0x0000' by default
        return classType(uint=result)
    
    def setOcta(self, address, value):
        self.set(address, Octa, value)
    
    def readOcta(self, address):
        return self.read(address, Octa)