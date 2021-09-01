#

def my_g():
    for i in {1, 2, 3}:
        #return i #здесь отработает только 1 раз, а yield
        yield i #здесь проходим сколько надо
#print(my_g()) # вариант с return

for n in my_g(): #для yield
    print(n)