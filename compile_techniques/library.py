def print_ln(s='', *args):
    print("----------using print_ln------------")
    print(s, *args)
    print("-----------end print_ln-------------")


class Instruction():
    def __init__(self):
        print("-------calling __init__ function of Instruction-------")

# Since ldi doesn't has __init__ function, it will call his father's __init__ method
class ldi(Instruction):
    print("ldi")

class cint():
    def __init__(self, val=None):
        print("---------calling cint class init function--------")
        print("value is: ", val)
        self.load()
    
    def load(self):
        ldi()