"""
    Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
написанную ранее функцию int_func().
    Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""

words = input('Введите слова только латинскими буквами, разделяя их пробелом и тоько в нижнем регистре: ')
if words.islower():
    words = words.title()
    print(words)
else:
    print('Не корректный ввод! Вводите данные, следуя инструкциям программы!')
