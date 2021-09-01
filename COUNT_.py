#

from itertools import count

for el in count(7):
    if el > 15: # 15 раз отшагает и успокоится, иначе бесконечность. можно дробно и с шагом  count(7.4, 1.012)
        break
    else:
        print(el)