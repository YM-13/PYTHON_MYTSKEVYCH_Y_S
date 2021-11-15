class TestClass:

    verion = 1

#print(dir(TestClass))  # mozno posmotret atributi classa
print(TestClass.verion)
print(id(TestClass.verion))

exm = TestClass() # exemplar class sozdaem takim obrazom
print(id(exm.verion)) # odin adres

exm2 = TestClass()
print(id(exm2.verion))
print(exm2.verion) # здесь выводится "1"

# МЕНЯЕМ ЗНАЧЕНИЕ АТРИБУТА КЛАССА СТР 17
TestClass.verion = 2 # ПЕРЕОПРЕДЕЛЯЕМ АТРИБУТ version КЛАССА для ниже следующих
print(exm2.verion) # здесь выводится уже ""2"

# ПЕРЕОПРЕДЕЛИМ АТРИБУТ version внутри экземпляра:
exm2.verion = 3
print(exm2.verion) # 3
print(exm.verion) # 2

TestClass.verion = 4
print(exm2.verion) # НЕ ВОСПРИНИМАЕТ ИЗМЕНЕНИЙ ИЗ-ЗА СТР 21 и ВЫВОДИТ "3"
print(exm.verion) # ВЫВОДИТ "4"

# СОЗДАЕМ МЕТОД ВНУТРИКЛАССА:

