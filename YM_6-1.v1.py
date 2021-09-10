"""
1. Создать класс TrafficLight (светофор).
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""
import time


class TrafficLight:
    red_sec = 7
    yel_sec = 2
    gre_sec = 7

    def __init__(self, r, y, g):
        while True:
            self.__color_r = r
            self.__color_y = y
            self.__color_g = g
            self.running()

    def running(self):
        print(self.__color_r, end='')
        time.sleep(self.red_sec)
        print('\r', end='')
        print(self.__color_y, end='')
        time.sleep(self.yel_sec)
        print('\r', end='')
        print(self.__color_g, end='')
        time.sleep(self.gre_sec)
        print('\r', end='')
        print(self.__color_y, end='')
        time.sleep(self.yel_sec)
        print('\r', end='')


t_l = TrafficLight(f"\033[31m\033[41mXXXXX\033[0m", f"\033[33m\033[43mXXXXX\033[0m",
                   f"\033[32m\033[42mXXXXX\033[0m")
t_l.running()

"""
https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html
https://en.wikipedia.org/wiki/ANSI_escape_code
https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
"""
