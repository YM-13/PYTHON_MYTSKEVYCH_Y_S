"""
Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
input().
"""
n = input("Enter number of elements : ")
list = n.split()
print(list)
len_list = len(list)
time = []
a = 0
new_list = []
if len_list % 2 != 0:
    time.append(list[-1])
    list.pop(-1)
    len_list -= 1
for i in list:
    x = list[0 + a]
    y = list[1 + a]
    x, y = y, x
    new_list.append(x)
    new_list.append(y)
    a += 2
    len_list -= 2
    if len_list <= 0:
        break
for i in time:
    new_list.append(i)
print(new_list)
