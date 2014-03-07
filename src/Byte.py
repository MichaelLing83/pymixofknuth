from bitstring import BitArray

class Byte:
    BYTE_SIZE_IN_BIT = 8
    def __init__(self, int=0, uint=0):
        self.byte = BitArray(length=Byte.BYTE_SIZE_IN_BIT, uint=0)
        self.length = self.byte.length
        if int!=0 and uint==0:
            self.byte.int = int
        elif int==0 and uint!=0:
            self.byte.uint = uint
        self.int = self.byte.int
        self.uint = self.byte.uint
        self.bin = self.byte.bin
        self.hex = self.byte.hex
    
    def __and__(self, another_byte):
        return Byte(uint=(self.byte & another_byte.byte).uint)
    
    def __or__(self, another_byte):
        return Byte(uint=(self.byte | another_byte.byte).uint)
    
    def __xor__(self, another_byte):
        return Byte(uint=(self.byte ^ another_byte.byte).uint)
    
    def __add__(self, another_byte):
        return Byte(int=(self.byte.int + another_byte.byte.int))
    
    def __sub__(self, another_byte):
        return Byte(int=(self.byte.int - another_byte.byte.int))
    
    def __eq__(self, another_byte):
        return self.byte.uint == another_byte.byte.uint
    
    def update(self, int=0, uint=0):
        if int!=0 and uint==0:
            self.byte.int = int
        elif int==0 and uint!=0:
            self.byte.uint = uint
        else:
            self.byte.int = 0
        self.int = self.byte.int
        self.uint = self.byte.uint
        self.bin = self.byte.bin
        self.hex = self.byte.hex