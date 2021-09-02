"""
Это модуль (библиотека), если запускать из другого файла с импортом этого модуля.
Если запускать здесь же, то это файл
"""
def simple():
    print('Hi!')

def calc():
    num = int(input("пиши число"))
    return num ** 15
#print(calc())


#if __name__ == "main":
#    print("I'm file")
#else:
#    print("I'm modul")
