"""
МЕТОД ВНУТРИ КЛАССА
"""
class TestClass:
    def get_name(self): # self делает из функции метод класса
        print("test")

print(TestClass.get_name) # СПРАВКА <function TestClass.get_name at 0x7f835129e8b0>

a = TestClass() # СОЗДАЛИ ЭКЗЕМПЛЯР КЛАССА
print(a.get_name) # СПРАВКА <bound method TestClass.get_name of <__main__.TestClass object at 0x7f835128beb0>>
