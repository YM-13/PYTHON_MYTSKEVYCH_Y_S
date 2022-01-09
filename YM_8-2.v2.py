"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException:

    def __init__(self, dividend=0, divider=0):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def check_op(date_str):
        dividend, divider = map(float, date_str.split(':'))
        try:
            print(dividend / divider)
        except ZeroDivisionError:
            print('На ноль делить нельзя, вводите данные корректно!')


dat_com = input('Введите выражение вида "40:2": ')
checker = MyException.check_op(dat_com)
