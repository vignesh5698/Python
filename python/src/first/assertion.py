'''
Created on Sep 5, 2017

@author: Vignesh
'''
def test(num):
    assert(num>=0),"Number greater than zero"
    return num
print(test(18))
print(test(-15))
#After assert fails,Remaining code will not be executed
print(test(55))