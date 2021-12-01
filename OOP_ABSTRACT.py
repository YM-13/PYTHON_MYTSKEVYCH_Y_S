
from abc import ABCMeta, abstractmethod

class Users(metaclass=ABCMeta):
    @abstractmethod
    def go_to(self):
        pass
    def read(self):
        pass

class Test(Users):
    def go_to(self):
        print("go_to")

    def read(self):
        print("read")

a = Test()
a.go_to()
a.read()