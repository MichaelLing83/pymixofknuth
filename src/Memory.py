from Byte import Byte

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