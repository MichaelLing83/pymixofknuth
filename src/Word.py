from bitstring import BitArray

class Word:
    WORD_SIZE_IN_BIT = 16   # bits
    def __init__(self, int=0, uint=0):
        self.Word = BitArray(length=Word.WORD_SIZE_IN_BIT, uint=0)
        self.length = self.Word.length
        if int!=0 and uint==0:
            self.Word.int = int
        elif int==0 and uint!=0:
            self.Word.uint = uint
        self.int = self.Word.int
        self.uint = self.Word.uint
        self.bin = self.Word.bin
        self.hex = self.Word.hex
    
    def __and__(self, another_Word):
        return Word(uint=(self.Word & another_Word.Word).uint)
    
    def __or__(self, another_Word):
        return Word(uint=(self.Word | another_Word.Word).uint)
    
    def __xor__(self, another_Word):
        return Word(uint=(self.Word ^ another_Word.Word).uint)
    
    def __add__(self, another_Word):
        return Word(int=(self.Word.int + another_Word.Word.int))
    
    def __sub__(self, another_Word):
        return Word(int=(self.Word.int - another_Word.Word.int))