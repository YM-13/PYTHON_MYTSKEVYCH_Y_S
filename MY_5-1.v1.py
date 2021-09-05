"""
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
"""
inp = input('Input: ')

while inp != '':
    stro = inp
    with open("hw1.txt", "a", encoding="utf-8") as your_t:
        your_t.writelines(f"{stro}s\n")
    inp = input('Input: ')
with open("hw1.txt", "r", encoding="utf-8") as your_txt:
    cont = your_txt.read()
    print(f'Вы ввели следующее:\n {cont}')
