'''
Created on Sep 6, 2017

@author: Vignesh
'''
def div(num1,num2):
    try:
        #if num2>0:
        num3=num1/num2
        return num3
    except ZeroDivisionError:
        print("Exception:Divide by Zero Error caught")
    except Exception:
        print("Exception caught")
    else:
        print(num3)

num1=int(input("Enter the Divident:"))
num2=int(input("Enter the Divisor:"))
div(num1,num2)
