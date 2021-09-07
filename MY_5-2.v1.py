"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""

with open("5-2.txt", "r", encoding="utf-8") as your_txt:
    cont = (your_txt.read())
    print(cont)
it = []
with open("5-2.txt", "r", encoding="utf-8") as your_txt:
    sent = your_txt.readlines()
    n_w = len(sent)
    print(f'В текстовом файле {n_w} стро(-ка, -ки, -к)\n')
    for i in sent:
        l = len(i.split())
        it.append(l)
    print(f'Ниже выведена информация в следующем порядке:\n"порядковый номер строки", "количество слов"')
    for i in enumerate(it, 1):
        print(i)
