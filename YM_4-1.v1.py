"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
время выполнения расчёта для конкретных значений необходимо запускать скрипт с
параметрами.
"""
from sys import argv
name, hours, const, add  = argv
h = int(hours)
c = int(const)
a = int(add)
def my_earn(argv):
    res = ((hours * const) + add)
    return res
print(my_earn(argv))

