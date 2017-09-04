'''
Created on Aug 31, 2017

@author: Vignesh
'''
#Opening a file
fo=open("FirstFile.txt","r+")
fo.write("Python is really Great...!!")
print("Name of the file is:",fo.name)
print("Closed :",fo.closed)
print("Mode:",fo.mode)
fo.close()
fo=open("FirstFile.txt","r")
str1=fo.read(50)
print(str1)
a=fo.tell();
print(a)

