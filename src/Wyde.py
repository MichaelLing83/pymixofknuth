from bitstring import BitArray

class Wyde:
    WYDE_SIZE_IN_BIT = 16   # bits
    def __init__(self, int=0, uint=0):
        self.Wyde = BitArray(length=Wyde.WYDE_SIZE_IN_BIT, uint=0)
        self.length = self.Wyde.length
        if int!=0 and uint==0:
            self.Wyde.int = int
        elif int==0 and uint!=0:
            self.Wyde.uint = uint
        self.int = self.Wyde.int
        self.uint = self.Wyde.uint
        self.bin = self.Wyde.bin
        self.hex = self.Wyde.hex
    
    def __and__(self, another_Wyde):
        return Wyde(uint=(self.Wyde & another_Wyde.Wyde).uint)
    
    def __or__(self, another_Wyde):
        return Wyde(uint=(self.Wyde | another_Wyde.Wyde).uint)
    
    def __xor__(self, another_Wyde):
        return Wyde(uint=(self.Wyde ^ another_Wyde.Wyde).uint)
    
    def __add__(self, another_Wyde):
        return Wyde(int=(self.Wyde.int + another_Wyde.Wyde.int))
    
    def __sub__(self, another_Wyde):
        return Wyde(int=(self.Wyde.int - another_Wyde.Wyde.int))