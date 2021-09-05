"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""
from typing import TextIO

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file1 = open("text_4.txt", "r") #, incoding="utf8")
while True:
    line = file1.readline()
    print(type(line))
    lin = line.split('\n')
    print(len(lin))
    if not line:
        break
    for key in my_dict.keys():
        print(key)
"""        if key = line[0]
    print(line.strip())
    
with open("text_4.txt", "r", incoding="utf8") as text:
    for i in
    cont = text.readline()
"""