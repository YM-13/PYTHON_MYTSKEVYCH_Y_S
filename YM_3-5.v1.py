"""
Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
"""

data = input(' Введите числа, разделяя их запятой: ').split(',')
data.sort()
r = 0
n_list = []
for i in data:
    i = float(i)
    if i == float(i):
    sum = r + i
    r = sum
    n_list.append(i)
print(sum)