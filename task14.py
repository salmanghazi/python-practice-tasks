from timeit import default_timer as timer
from datetime import timedelta
import time


class makeSingleton:
    def __init__(self, cls):
        self._cls = cls

    def getInstance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError("use getInstance() method only")

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@makeSingleton
class myClass:
    def __init__(self):
        pass

    def getString(self):
        pass

    def printString(self):
        return self


# Testing Decorator
my1 = myClass.getInstance()
print(my1.printString())

my12 = myClass.getInstance()
print(my12.printString())
