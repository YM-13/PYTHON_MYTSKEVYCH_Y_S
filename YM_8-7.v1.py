"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
"""


class Complex_num:

    def __init__(self, z1, z2):
                self.z1 = z1
                self.z2 = z2

    @staticmethod
    def addition(z1, z2):
        data = list(z1 + z2)
        time_num = []
        list_num = []

        while data != []:
            a = data.pop(0)
            if a != str('(') and a != str(')') and a != str('+') and a != str('-'):
                time_num.append(a)
            elif a == str('-') or a == str('+'):
                time_num = ''.join(time_num)
                list_num.append(float(time_num))
                time_num = []
                list_num.append(f'{a}') # что-то здесь не так
        time_num = ''.join(time_num)
        list_num.append(float(time_num))
        print(sum(list_num))


n = Complex_num.addition('(61+2)', '(4+21)')
print(n.addition())
