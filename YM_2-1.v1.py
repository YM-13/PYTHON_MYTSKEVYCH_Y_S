'''
 Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
 каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у
 пользователя, а указать явно, в программе.
'''
list = [True, None]

n_int = 13
list.append(n_int)
n_float = 36.6
list.append(n_float)
n_complex = (36.6 + 13j)
list.append(n_complex)
data_str = 'pink'
list.append(data_str)
data_list = ['cat', 22]
list.append(data_list)
data_tuple = (22, 'clouse', 45.3)
list.append(data_tuple)
data_set = {'dog', 55}
list.append(data_set)
data_dict = {1: 'january'}
list.append(data_dict)

print(f'Список содержит следующие данных: {list}')
print('Покажем к какому типу данных относятся элементы из списка:')
for ind, el in enumerate(list, 1):
    print(f'{ind}) {el} - {type(el)}')
