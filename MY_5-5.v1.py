"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
inp = input('Введите числа, разделяя их пробелом: ')

with open("5-5.txt", "w", encoding="utf-8") as your_t:
    your_t.writelines(inp)
with open("5-5.txt", "r", encoding="utf-8") as dc:
    data = (dc.readline()).split()
    calc = [float(i) for i in data]
    print(f'Результат сложения: {sum(calc)}')
