"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
с декоратором @classmethod.  Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:  # добавить если проверка статик метода фолс, то прекратить работу

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def check_date(date_str):
        day, month, year = map(int, date_str.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        re_date = cls(day, month, year)
        return re_date

dat_com = input('Введите дату в формате дд-мм-гг: ')
checker = Date.check_date(dat_com)
new_view = Date.from_string(dat_com)
print(checker)
print(new_view.day, new_view.month, new_view.year)
