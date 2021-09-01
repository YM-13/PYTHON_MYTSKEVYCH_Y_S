#
from itertools import cycle

c = 0
for el in cycle(["ABC", False, 4.6]):
    if c > 10:
        break
    print(el)
    c += 1
