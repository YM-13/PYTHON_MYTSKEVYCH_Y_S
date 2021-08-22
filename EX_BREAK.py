"""num = int(input('Введите число от 0 до 10: '))

while num < 0 or num > 10:
    print('Вы ввели не правльное число. Введите число от 0 до 10: ')
    num = int(input('Введите число от 0 до 10: '))

print(f'{num ** 2}')"""

while True:
    num = int(input('Введите число от 0 до 10: '))
    if num > 0 and  num < 10:
        print(num ** 2)
        break
    else:
        print('INCORRECT. Введите число от 0 до 10: ')



