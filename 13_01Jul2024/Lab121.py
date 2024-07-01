#abstractmethod

from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Saurabh(Father):
    def loan(self):
        print("Saurabh has a loan")

d1 = Saurabh("D1")
d1.loan()