'''
    Programme dynamic class and object
    Author : mAk
    CopyRight: 2020

'''
import random
class Enemy:
    hp = 200
    def __init__(self,atkl,atkh):
        self.atkl = atkl
        self.atkh = atkh
    def getAtk(self):
        print(self.atkl)
    def getHp(self):
        print("Hp is",self.hp)

enm1 = Enemy(10,100)
enm1.getAtk()
enm1.getHp()
