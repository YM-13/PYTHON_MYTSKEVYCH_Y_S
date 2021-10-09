def dek(f):
    def wrapper():
        return "<b>" + f() + "</b>"
    return wrapper


@dek
def my_f():
    return "Hello"


print(my_f())
# print(help(my_f))