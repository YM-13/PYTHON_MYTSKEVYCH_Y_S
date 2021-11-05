class Complex_num:
    def __init__(self, z1, z2):
        self.z1 = z1
        self.z2 = z2

    # @staticmethod
    def addition(self):
        s_1 = eval(self.z1)
        s_2 = eval(self.z2)
        return s_1 + s_2


n = Complex_num('(61+2)', '(4+21)')
print(n.addition())
print(complex(61, 2) + complex(4, 21))