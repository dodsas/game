import sys
from abc import ABC, abstractmethod

# def my_exception_handler(exc_type, exc_value, traceback):
#     dun_print.errorf("TEST")

# sys.excepthook = my_exception_handler

# test.test()

class MyInterface(ABC):
    @abstractmethod
    def do_something(self):
        pass

class MyClass(MyInterface):
    def do_something(self):
        # MyClass에서 MyInterface의 do_something 메서드를 구현합니다.
        # ...
        print("aa")

class MyClass2(MyInterface):
    def do_something(self):
        # MyClass에서 MyInterface의 do_something 메서드를 구현합니다.
        # ...
        print("aa2")

list = [MyClass(), MyClass2()]

# loop through the list
for item in list:
    # call the do_something method
    item.do_something()