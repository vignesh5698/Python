'''
Created on Aug 28, 2017

@author: Vignesh
'''
def Var_len(arg,*var1):
    print("Output is")
    print(arg)
    for a in var1:
        print(a)
    return
Var_len(10) 
Var_len(10,20,30)
Var_len(10,20,30,500)
li=[100,25,58,46]
Var_len(li)
