print('СОРЕВНОВАНИЯ ПО ПАЙТОНУ')
count = int(input('Введите количество учвстников: '))
i = count
members = []

while i > 0:
    name = input(f'Кто занял {i} место?')
    members.append(name)
    i -= 1
print('В соревновании участвовали: ', members)
members.reverse()
result = members  [:3]
result = f'Победители: {result}. Поздравляем'
print(result)