'''
Created on Sep 7, 2017

@author: Vignesh
'''
class Test1:
    def __init__(self,x):
        self.number=x
    
    def square(self):
        val=self.number*self.number
        print(val)

a=int(input("Enter the number:"))
ob1=Test1(a)
ob1.square()
