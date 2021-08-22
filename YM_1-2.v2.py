"""
№ 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

seconds = int(input('Пожалуйста, введите время в секундах: '))
hour = seconds // 3600
minutes = (seconds - hour * 3600) // 60
seconds_rest = seconds - hour * 3600 - minutes * 60

print(f'{hour:02}:{minutes:02}:{seconds_rest:02}')