from random import *
from statistics import *

class MyObject():
    def __init__(self):
        self.numbers = choices(range(101), k=500)
    def MINIMALNY(self):
        return min(self.numbers)
    def MAXYMALNY(self):
        return max(self.numbers)
    def SUMUJE(self):
        return sum(self.numbers)
    def ODCHYLENIE(self):
        return stdev(self.numbers)
    def MSU(self):
        return mode(self.numbers)
    def MDU(self):
        return median(self.numbers)
    def ZAPISUJE(self):
        self.filename = str(self.numbers[0]) + '.txt'
        with open(self.filename, 'w') as file:
            file.write(str(self.MINIMALNY()) + ' ')
            file.write(str(self.MAXYMALNY()) + ' ')
            file.write(str(self.SUMUJE()) + ' ')
            file.write(str(self.ODCHYLENIE()) + ' ')
            file.write(str(self.MSU()) + ' ')
            file.write(str(self.MDU()) + ' ')

a = MyObject()
a.ZAPISUJE()