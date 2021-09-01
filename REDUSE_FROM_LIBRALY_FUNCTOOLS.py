# 02:00:00
from functools import reduce

def my_func(el_1, el_2):
    return el_1 + el_2

print(reduce(my_func, [10, 20, 30]))