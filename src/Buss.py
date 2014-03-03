
class Buss:
    '''
    Buss class represents a buss connection between two components, which is composed of a set of pins. Each pin is a boolean value, and True stands for high voltage, and False stands for low voltage.
    '''
    def __init__(self, pin_default_state=False):
        '''
        '''
        self.pins = list()
        self.pin_names = dict()
        self.pin_default_state = pin_default_state
    
    def add_pin(self, pin_index, pin_name):
        '''
        '''
        assert pin_index>=len(self.pins), "pin_index=%d is already defined!" % pin_index
        assert pin_name not in self.pin_names.keys(), "pin_name=%s is already defined!" % pin_name
        self.pins.append(self.pin_default_state)
        self.pin_names[pin_name] = pin_index

if __name__ == '__main__':
    print("Buss class test!")
    buss = Buss()
    buss.add_pin(0, "valid")
    print(buss.pins)
    print(buss.pin_names)