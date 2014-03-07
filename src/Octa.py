from bitstring import BitArray

class Octa:
    TETRA_SIZE_IN_BIT = 64   # bits
    def __init__(self, int=0, uint=0):
        self.octa = BitArray(length=Octa.TETRA_SIZE_IN_BIT, uint=0)
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