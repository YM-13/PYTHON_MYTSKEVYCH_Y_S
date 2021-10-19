"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):

    def __init__(self, dividend=0, divider=0):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def check_op(date_str):
        dividend, divider = map(float, date_str.split(':'))
        try:
            if divider == 0:
                raise MyException('На ноль делить нельзя, вводите данные корректно!')
        except (ValueError, MyException) as err:  # ZeroDivisionError
            print(err)
        else:
            print(dividend / divider)
"""
    @classmethod
    def from_string(cls, date_str):
        dividend, divider = map(float, date_str.split(':'))
        nums = cls(dividend, divider)
        return dividend / divider
"""

dat_com = input('Введите выражение вида "40:2": ')
checker = MyException.check_op(dat_com)
#new_view = MyException.from_string(dat_com)
#print(checker)
#print(new_view)
