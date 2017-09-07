'''
Created on Sep 7, 2017

@author: Vignesh
'''
class first:
    life=3
    def attack(self):
        print("Attacked")
        self.life-=1
    def checkLife(self):
        if self.life<=0:
            print("You have no life..")
        else:
            print("life left:"+str(self.life))
ob1=first()
ob1.attack()
ob1.checkLife()
ob2=first()
ob2.attack()
ob2.attack()
ob2.attack()
ob2.checkLife()  
            
        