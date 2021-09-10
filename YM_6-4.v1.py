"""
4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""


class Car:

    def __init__(self, s, c, n):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = True

    #        self.dir = di

    def go(self):
        print(f'\nThe car {self.name} started moving!')

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed}km/h')

    def stop(self):
        print(f'The car {self.name} has stopped!\n')

    def turn_direction(self, cd):
        self.cdir = cd
        print(f'{self.name} goes {self.cdir}')


class TownCar(Car):  # Или заменить скорость на другую
    def __init__(self, s, c, n, p):
        super().__init__(s, c, n)
        self.pred = p

    def speed_exceeded_tc(self):
        if self.speed > self.pred:
            print(f'{self.color} {self.name}, REDUCE YOUR SPEED!!! You are speeding!!! '
                  f'Your speed is {self.speed} km/h! Overspeeding is {float(self.speed) - float(self.pred)} km/h!!!')


class WorkCar(Car):
    def __init__(self, s, c, n, p):
        super().__init__(s, c, n)
        self.pred = p

    def speed_exceeded_wc(self):
        if self.speed > self.pred:
            print(f'{self.color} {self.name}, REDUCE YOUR SPEED!!! You are speeding!!! '
                  f'Your speed is {self.speed} km/h! Overspeeding is {float(self.speed) - float(self.pred)} km/h')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def ppp(self, tt):
        print(f'\n{tt} is chasing someone!!!')


car_1_porsh = TownCar(100, "BLACK", "PORSHE", 60)
car_1_porsh.go()
car_1_porsh.show_speed()
car_1_porsh.speed_exceeded_tc()
car_1_porsh.turn_direction("LEFT")
car_1_porsh.stop()

car_2_mers = WorkCar(90, "WHITE", "MERSEDES", 40)
car_2_mers.speed_exceeded_wc()

car_3_bmw = SportCar(140, "BLUE", "M5")
car_3_bmw.go()

pc = PoliceCar(70, "BLACK AND WHITE", "FORD")
pc.ppp("POLICE CAR")
