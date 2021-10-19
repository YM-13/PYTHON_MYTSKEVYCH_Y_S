class MyClass:
    def m_1(self):
        print("Hi")

    @staticmethod
    def m_2():
        print("Python")
        return MyClass().m_1()

    @classmethod
    def m_3(cls):
        print("Py Py") #внешнее взаимодействие
        return cls.m_2() #внутреннее взаимодействие

first = MyClass(88)
first.m_1()
first.m3()
