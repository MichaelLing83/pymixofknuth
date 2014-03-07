from bitstring import BitArray

class Tetra:
    TETRA_SIZE_IN_BIT = 32   # bits
    def __init__(self, int=0, uint=0):
        self.Tetra = BitArray(length=Tetra.TETRA_SIZE_IN_BIT, uint=0)
        self.length = self.Tetra.length
        if int!=0 and uint==0:
            self.Tetra.int = int
        elif int==0 and uint!=0:
            self.Tetra.uint = uint
        self.int = self.Tetra.int
        self.uint = self.Tetra.uint
        self.bin = self.Tetra.bin
        self.hex = self.Tetra.hex
    
    def __and__(self, another_Tetra):
        return Tetra(uint=(self.Tetra & another_Tetra.Tetra).uint)
    
    def __or__(self, another_Tetra):
        return Tetra(uint=(self.Tetra | another_Tetra.Tetra).uint)
    
    def __xor__(self, another_Tetra):
        return Tetra(uint=(self.Tetra ^ another_Tetra.Tetra).uint)
    
    def __add__(self, another_Tetra):
        return Tetra(int=(self.Tetra.int + another_Tetra.Tetra.int))
    
    def __sub__(self, another_Tetra):
        return Tetra(int=(self.Tetra.int - another_Tetra.Tetra.int))