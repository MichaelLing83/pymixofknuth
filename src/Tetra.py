from bitstring import BitArray

class Tetra:
    SIZE_IN_BIT = 32   # bits
    def __init__(self, int=0, uint=0):
        self.tetra = BitArray(length=Tetra.SIZE_IN_BIT, uint=0)
        self.length = self.tetra.length
        if int!=0 and uint==0:
            self.tetra.int = int
        elif int==0 and uint!=0:
            self.tetra.uint = uint
        self.int = self.tetra.int
        self.uint = self.tetra.uint
        self.bin = self.tetra.bin
        self.hex = self.tetra.hex
    
    def __and__(self, another_Tetra):
        return Tetra(uint=(self.tetra & another_Tetra.tetra).uint)
    
    def __or__(self, another_Tetra):
        return Tetra(uint=(self.tetra | another_Tetra.tetra).uint)
    
    def __xor__(self, another_Tetra):
        return Tetra(uint=(self.tetra ^ another_Tetra.tetra).uint)
    
    def __add__(self, another_Tetra):
        return Tetra(int=(self.tetra.int + another_Tetra.tetra.int))
    
    def __sub__(self, another_Tetra):
        return Tetra(int=(self.tetra.int - another_Tetra.tetra.int))
    
    def __eq__(self, another_Tetra):
        return self.tetra.uint == another_Tetra.tetra.uint
    
    def update(self, int=0, uint=0):
        if int!=0 and uint==0:
            self.tetra.int = int
        elif int==0 and uint!=0:
            self.tetra.uint = uint
        else:
            self.tetra.int = 0
        self.int = self.tetra.int
        self.uint = self.tetra.uint
        self.bin = self.tetra.bin
        self.hex = self.tetra.hex