'''
Created on Aug 30, 2017

@author: Vignesh
'''

#Type the following code in text editor and save as fib.py 
def fib(n): # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b   
    print()


#Run this Code in python interpreter
>>>import fib 
>>>fib.fib(1000)