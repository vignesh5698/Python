'''
Created on Aug 25, 2017

@author: Vignesh
'''
str="google"
li=['Mac','Win','Linux']
num=int(input("Enter the Number:"))
#if
if num%2==0:
    print("The Number is Even number")
else:
    print("The Number is Odd")
n1=0
#while
while n1<num:
    print(n1+1)
    n1=n1+1
#for
#As like Enhanced for loop in java-Traversal
for a in range(num):  #Range() commences from 0
    print(a+1)
for char1 in str:
    print(char1,end=" ")
    z=1
print()
    
for a in li:
    print(a)            