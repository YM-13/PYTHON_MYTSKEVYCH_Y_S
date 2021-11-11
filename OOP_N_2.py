"""

"""

class TestClass:
    version = 1

exm = TestClass()
exm2 = TestClass()


dir(exm)
#print(dir())

id(exm.version)
#print(id(exm.version))
#print(id(TestClass.version))

TestClass.version = 2 #меняем значение, переопределяем атрибут класса
#print(exm2.version)

exm2.version = 3

TestClass.version = 4

print(exm.version)
print(exm2.version)