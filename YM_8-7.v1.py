"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
"""


class Complex_num:

    def __init__(self, data):  # z1, m, z2):
        #        self.z1 = z1
        #        self.m = m
        #        self.z2 = z2
        self.data = data

    @staticmethod
    def addition(data):  # (z1, m, z2):
        list_num = []
        l1 = []
        lis = list(data)  # .split(' ')
        while lis != []:
            a = lis.pop(0)
            if a != str('(') and a != str(')'):
                if a != str('+') and a != str('-'):
                    list_num.append(a)   #(lis[0])
                l1 = ''.join(list_num)
                continue
        return sum(z1, )
"""
    #        z1 = z1.split()
    #        z2 = z2.split(' ')
    for i in range(data):
        if i != '(' or ')':
            list_num.append(i)

    cont = z1 + z2
    return cont
"""

"""    def __init__(self, data_str):
        z_1, z_2 = map(float(data_str.split(':')))
        self.data_str = data_str
"""

n = Complex_num.addition('(61+2) + (4+21)')
print(n.addition())
