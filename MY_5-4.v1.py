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
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file1 = open("text_4.txt", "r")
while True:
    line = file1.readline()
    lin = line.split()
    if not line:
        break
    c = lin[0]
    for key in my_dict.keys():
        if key == c:
            ch = my_dict[key]
            lin[0] = ch
            lin = ' '.join(lin)
            with open("text_4-1.txt", "a", encoding="utf-8") as sentens:
                text = sentens.write(f'{lin}\n')
    continue
