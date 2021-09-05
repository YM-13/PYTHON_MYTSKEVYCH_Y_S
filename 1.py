#dem = input('Вводите данные для записи в файл текстового формата. '
#           'По окончании ввода нажмите "e"+"enter"')
import json

data_in = input('Вводите данные для записи в файл текстового формата. '
            'По окончании ввода нажмите "e"+"enter": ').split(',')
while data_in != " ":
    data = json.loads(data_in)
    with open("hw1.txt", "a", encoding="utf-8") as your_t:
        your_t.writelines(f"[{data_in}]s\n")
    data_in = input('Вводите данные для записи в файл текстового формата. '
                    'По окончании ввода нажмите "e"+"enter": ').split(',')
with open("hw1.txt", "r", encoding="utf-8") as info:
    cont = info.read()
    print(cont)


