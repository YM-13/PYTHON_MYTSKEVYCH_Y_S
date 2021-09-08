#  00:38:00

class MyAuto:
    pass # тк после ауто энтр, а энтр это тело функции, нам не надо/можно коменты
    #name = "Lexus" # атрибуты класса - это переменные, которые располагаются в теле класса
    #model = "RX 350L" # они как глобальные переменные в контексте  в контексте, за пределами мы их не видим
    #year = 2021
    a_count = 0


    # конструктор
    # атрибуты объекта
    def __init__(self, n, m, y): # нужно показать переменные для других тоже:
        self.name = n
        self.model = m
        self.year = y
        MyAuto.a_count += 1
        print(n, m, y)

    def on_start(self):  # МЕТОДЫ. self - ссылка на объект, на его место встает объект.
        print(f"Go - go car {self.name}!!!")               # Внутри класса помогает взаимодействовать. Все функции применяются
    def on_stop(self):
        print("Stop.")

# ОБЪЕКТ.   ИХ МОЖЕТ БЫТЬ НЕОГРАНИЧЕННОЕ КОЛИЧЕСТВО
auto_1 = MyAuto("Mazda", "CX9", 2021)
print(auto_1.a_count)
"""auto_1.name = "Mazda" # ЗАМЕНА ИМЕНИ ТОЛЬКО К ЭТОМУ ОБЪЕКТУ. ДАЛЬШЕ БУДЕТ LEXUS
print(auto_1.name)
auto_1.on_start()"""
auto_2 = MyAuto("Lada", "XRay", 2020)
print(auto_2.a_count)
#auto_1.on_start()