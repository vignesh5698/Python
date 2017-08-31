'''
Created on Aug 29, 2017

@author: Vignesh
'''
import random
import math
# First random number
print ("random() : ", random.random())
# Second random number
a=random.random()
print(math.ceil(a*100))
#seed
random.seed()
print(random.random())
random.seed(100)
print(random.random())
#shuffle
li=[10,20,50,42,11,24,31,99]
random.shuffle(li)
print("ReShuffled list",li)
#uniform
print(random.uniform(2,4))
print ("tan(0) : ", math.tan(0))