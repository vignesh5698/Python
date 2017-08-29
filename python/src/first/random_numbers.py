'''
Created on Aug 29, 2017

@author: Vignesh
'''
import random
from random import randrange
a=[5,6,9,8]
print(random.choice(a))
b=randrange(2)
print(b)
print(randrange(200))
c=input("Enter the number:")
if b==c:
    print("You have Entered Correct Number")
else:
    print("Good try..!!")
    print("But answer is",b)