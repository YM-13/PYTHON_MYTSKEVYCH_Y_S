"""
stdin
f = 6564424525
g = 323252462

# 6887676987
# 6241172063
# 2121966389319430550

1)
n = int(input())
d = []
if n > 0:
    while n != 0:
        n = (n - 1)
        d.append(n ** 2)
    d.reverse()

print(*d, sep='\n')

2)
def is_leep(year):
    leep = False

    if year < 1900 or year > 100000:
        print("Incorrect data")
    if (year % 4) != 0:
        leep = False
        return leep
    elif (year % 100) != 0:
        leep = True
        return leep
    elif (year % 400) == 0:
        leep = True
        return leep
    leep = False
    return leep

year = int(input("Введите год: "))
"""
"""
n = 90
b = []
if 1 <= n <= 150:
    for i in range(1, n + 1):
        b.append(i)

print(*b, sep='')
"""

