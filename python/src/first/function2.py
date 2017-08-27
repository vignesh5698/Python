'''
Created on Aug 28, 2017

@author: Vignesh
'''
def funcName(name="Default",age=100):
    "This is Example for function with Arguments"
    print("Name:",name)
    print("Age",age)
    return
name="Vignesh"
age=20
funcName(name,age)
funcName(name="Java", age=26)
#We can change the parameters's position
funcName(age=12,name="Thomas Suarez")
#if we change parameter for already defined variable,it directly assigns to function parameter 
funcName(age, name) #check output
#Default Parameter
funcName(name="James Gosling")
