'''
Created on Sep 5, 2017

@author: Vignesh
'''
try:
    fo=open("tes.txt","r")
    fo.write("This cannot be added")
#Generic Exception
except Exception:
    print("Exception Caught")
else:
    print("Written successfully")
    