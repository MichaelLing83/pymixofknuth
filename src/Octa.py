from bitstring import BitArray

class Octa:
    SIZE_IN_BIT = 64   # bits
    def __init__(self, int=0, uint=0):
        self.octa = BitArray(length=Octa.SIZE_IN_BIT, uint=0)
        self.length = self.octa.length
        if int!=0 and uint==0:
            self.octa.int = int
        elif int==0 and uint!=0:
            self.octa.uint = uint
        self.int = self.octa.int
        self.uint = self.octa.uint
        self.bin = self.octa.bin
        self.hex = self.octa.hex
    
    def __and__(self, another_Octa):
        return Octa(uint=(self.octa & another_Octa.octa).uint)
    
    def __or__(self, another_Octa):
        return Octa(uint=(self.octa | another_Octa.octa).uint)
    
    def __xor__(self, another_Octa):
        return Octa(uint=(self.octa ^ another_Octa.octa).uint)
    
    def __add__(self, another_Octa):
        return Octa(int=(self.octa.int + another_Octa.octa.int))
    
    def __sub__(self, another_Octa):
        return Octa(int=(self.octa.int - another_Octa.octa.int))
    
    def __eq__(self, another_Octa):
        return self.octa.uint == another_Octa.octa.uint
    
    def update(self, int=0, uint=0):
        '''
        Update the value of this Octa object. Note that parameter int and uint are exclusive.

        @int=0 (int): update with an signed integer value.
        @uint=0 (int): update with an unsigned integer value.

        @return (null)
        '''
        if int!=0 and uint==0:
            self.octa.int = int
        elif int==0 and uint!=0:
            self.octa.uint = uint
        else:
            self.octa.int = 0
        self.int = self.octa.int
        self.uint = self.octa.uint
        self.bin = self.octa.bin
        self.hex = self.octa.hex