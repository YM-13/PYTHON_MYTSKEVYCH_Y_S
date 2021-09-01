def my_func():
    data = input(' Введите числа, разделяя их запятой: ').split(',')
    s = 0
    let = []
    c = len(data)
    for i in data:
        i = float(i)
        s = i + s

    return s
print(my_func())



