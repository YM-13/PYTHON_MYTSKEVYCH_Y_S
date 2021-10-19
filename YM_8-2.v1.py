"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Exception:

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
checker = Exception.check_date(dat_com)
new_view = Exception.from_string(dat_com)
print(checker)
print(new_view.day, new_view.month, new_view.year)