from kot import *
from pies import *
from papuga import *

class Zwierzyniec:
    kot = Kot()
    pies = Pies()
    papuga = Papuga()


    def dajGlos(self):
        return f'{self.kot.dajGlos()}\n{self.pies.dajGlos()}\n{self.papuga.dajGlos()}'

a = Zwierzyniec()

print(a.dajGlos())

