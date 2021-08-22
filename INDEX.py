top5 = 'Первые 5 мест на соревнованиях: 1.Ivanov 2.Petrov 3.Sidorov 4.Rubens 5.Kolins'

r = top5.find('1')
w = top5.find('4')

top3 = top5[r:w]

result = (f'Congratulation {top3.upper()} с победой')
print(result)
