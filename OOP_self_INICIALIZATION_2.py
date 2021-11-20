"""
self общепринят програмистами, если вместо него по схеме писать, например, test, то работать будет,
но код будет не понятен другим программистам
"""
class User:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        print(self.args)
        print(self.kwargs) #

a = User(*[1, 2, 3]) # args - ПРИНИМАЕМ СПИСОК И РАСПАКОВЫВАЕМ ЕГО В КОРТЭЖ, а kwargs - пуст

a = User(*[1, 2, 3], **{"name": "name1"})
"""
b = User("b")

b.name = 10 # ПЕРЕОПРЕД. АРГ-Т "name" ВНУТРИ ЭКЗ-А "b"

print(b.name) # ВЫВЕДЕТ ОПРЕД-Й АТРИБУТ "name" "a"
print(a.name) # ВЫВЕДЕТ ПЕРЕОПРЕД-Й АТРИБУТ "name" "10"
"""