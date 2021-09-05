"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""

inp = input('Input: ')

while inp != '':
    stro = inp
    with open("5-2.txt", "a", encoding="utf-8") as your_t:
        your_t.writelines(f"{stro}s\n")
    inp = input('Input: ')
with open("5-2.txt", "r", encoding="utf-8") as your_txt:
    cont = your_txt.read()
    print(f'Вы ввели следующее:\n {cont}')