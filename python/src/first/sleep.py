'''
Created on Sep 9, 2017

@author: Vignesh
'''
import turtle
from time import sleep

win=turtle.Screen()
pen=turtle.Turtle()
pen.color("red")

i=0
while True:
    pen.forward(100)
    pen.right(90)
    print("Hello")
    sleep(1)
    print("After Sleep")
    sleep(1)