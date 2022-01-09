"""
№ 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
seconds = int(input('Пожалуйста, введите время в секундах: '))
hour = seconds // 3600
minutes = (seconds - hour * 3600) // 60
seconds_rest = seconds - hour * 3600 - minutes * 60

if hour < 10 and minutes < 10 and seconds_rest < 10:
    print(f"Отображаем {seconds} секунд(ы) в формате отображения времени чч:мм:сс - 0{hour}:0{minutes}:0{seconds_rest}")

elif hour < 10 and minutes < 10 and seconds_rest >= 10:
    print(f"Отображаем {seconds} секунд(ы) в формате отображения времени чч:мм:сс - 0{hour}:0{minutes}:{seconds_rest}")

elif hour >= 10 and minutes >= 10 and seconds_rest >= 10:
    print(f"Отображаем {seconds} секунд(ы) в формате отображения времени чч:мм:сс - {hour}:{minutes}:{seconds_rest}")

elif hour >= 10 and minutes < 10 and seconds_rest < 10:
    print(f"Отображаем {seconds} секунд(ы) в формате отображения времени чч:мм:сс - {hour}:0{minutes}:0{seconds_rest}")

elif hour >= 10 and minutes >= 10 and seconds_rest < 10:
    print(f"Отображаем {seconds} секунд(ы) в формате отображения времени чч:мм:сс - {hour}:{minutes}:0{seconds_rest}")

elif hour < 10 and minutes >= 10 and seconds_rest < 10:
    print(f"Отображаем {seconds} секунд(ы) в формате отображения времени чч:мм:сс - 0{hour}:{minutes}:0{seconds_rest}")

elif hour >= 10 and minutes < 10 and seconds_rest >= 10:
    print(f"Отображаем {seconds} секунд(ы) в формате отображения времени чч:мм:сс - {hour}:0{minutes}:{seconds_rest}")

elif hour < 10 and minutes >= 10 and seconds_rest >= 10:
    print(f"Отображаем {seconds} секунд(ы) в формате отображения времени чч:мм:сс - 0{hour}:{minutes}:{seconds_rest}")
