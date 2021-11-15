class User:
    name = "Test"
    age = 17

print(User.name)

print(getattr(User, "name")) # ЭТА ФУНКЦИЯ ТАКЖЕ ВЫВОДИТ ЗНАЧЕНИЕ