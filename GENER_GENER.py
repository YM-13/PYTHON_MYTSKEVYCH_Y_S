#GENERATOR GENERATOR. Это конструкция которая не имеет веса. Это формула, по которой
# он будет работать интерактивно,пошагово, по одному

new_1 = (n ** 3 for n in range(1, 11))
print(new_1)

# 2

new_2 = (n ** 3 for n in range(1, 1_000_000_000))
print(new_2)

for i in new_2:
    print(i)

# 3 01:50:00  print с islice продолжил распаковку после 3 предыдущих. Можно пройти только 1 раз цикла
from itertools import islice

new_2 = (n ** 3 for n in range(1, 11))
print(new_2)
print(next(new_2))
print(next(new_2))
print(next(new_2))

print(*islice(new_2, 4))