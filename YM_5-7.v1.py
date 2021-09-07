"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

tot = []
for_dict_p = []
num_p = []
dict_p = {}

for_dict_dam = []
num_dam = []
dict_dam = {}

num_for_eve = []
dict_eve = {}
с = 0
data = open("text_7.txt", "r")
while True:
    strip = data.readline()
    if strip == "\n":
        continue
    strip = strip.split()
    if len(strip) == 0:
        break
    res = int(strip[2])
    spe = int(strip[3])
    sub = res - spe
    if sub > 0:  # ПРИБЫЛЬНЫЕ
        с += 1
        num_p = [sub]
        num_for_eve.append(sub)
        key_1 = str(strip[0])
        key_2 = str(strip[1])
        for_dict_p = [f'{key_2} "{key_1}"']
        dict_p.update(zip(for_dict_p, num_p))
        for_dict_p.clear()
        num_p.clear()
    if sub < 0:  # УБЫТОЧНЫЕ
        num_dam = [sub]
        key_1 = str(strip[0])
        key_2 = str(strip[1])
        for_dict_dam = [f'{key_2} "{key_1}"']
        dict_dam.update(zip(for_dict_dam, num_dam))
        for_dict_dam.clear()
        num_dam.clear()
nu_ev = [sum(num_for_eve) / с]  # кол-во прибыльных фирм
name = ['Средняя прибыль']
dict_eve.update(zip(name, nu_ev))
tot.append(dict_p)
tot.append(dict_dam)
tot.append(dict_eve)
with open("text78.json", "w", encoding="utf-8") as write_f:
    json.dump(tot, write_f)
data.close()
