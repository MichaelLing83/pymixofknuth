from bitstring import BitArray

class Wyde:
    SIZE_IN_BIT = 16   # bits
    def __init__(self, int=0, uint=0):
        self.wyde = BitArray(length=Wyde.SIZE_IN_BIT, uint=0)
        self.length = self.wyde.length
        if int!=0 and uint==0:
            self.wyde.int = int
        elif int==0 and uint!=0:
            self.wyde.uint = uint
        self.int = self.wyde.int
        self.uint = self.wyde.uint
        self.bin = self.wyde.bin
        self.hex = self.wyde.hex
    
    def __and__(self, another_Wyde):
        return Wyde(uint=(self.wyde & another_Wyde.wyde).uint)
    
    def __or__(self, another_Wyde):
        return Wyde(uint=(self.wyde | another_Wyde.wyde).uint)
    
    def __xor__(self, another_Wyde):
        return Wyde(uint=(self.wyde ^ another_Wyde.wyde).uint)
    
    def __add__(self, another_Wyde):
        return Wyde(int=(self.wyde.int + another_Wyde.wyde.int))
    
    def __sub__(self, another_Wyde):
        return Wyde(int=(self.wyde.int - another_Wyde.wyde.int))
    
    def __eq__(self, another_Wyde):
        return self.wyde.uint == another_Wyde.wyde.uint
    
    def update(self, int=0, uint=0):
        if int!=0 and uint==0:
            self.wyde.int = int
        elif int==0 and uint!=0:
            self.wyde.uint = uint
        else:
            self.wyde.int = 0
        self.int = self.wyde.int
        self.uint = self.wyde.uint
        self.bin = self.wyde.bin
        self.hex = self.wyde.hex