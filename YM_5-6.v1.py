"""
Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

for_dict = []
for_dict2 = []
dict = {}
data = open("text_6.txt", "r")
while True:
    strip = data.readline()
    if strip == "\n":
        continue
    strip = strip.split()
    if len(strip) == 0:
        break
    key = strip.pop(0)
    for_dict.append(key)
    st = strip
    for ii in st:
        num = [i for i in ii if i.isdigit()]
        if not num:
            continue
        for_dict2.append(int(''.join(num)))
    for_dict2 = [sum(for_dict2)]
    dict.update(zip(for_dict, for_dict2))
    for_dict.clear()
    for_dict2.clear()
    continue
print(f'Выводим содержание словаря:\n{dict}')
data.close()
