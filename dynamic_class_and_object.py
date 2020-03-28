import random
class Enemy:
    def __init__(self,atkl,atkh):
        self.atkl = atkl
        self.atkh = atkh
    def getAtk(self):
        print(self.atkl)

enm1 = Enemy(10,100)
enm1.getAtk()
