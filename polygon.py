from math import *
import turtle
t = turtle.Turtle()
def varlength(n,A):
    b = ((2*A)/(n*sin(radians(360/n))))**0.5
    length = ((2*(b**2))+((-2*(b**2))*(cos(radians(360/n)))))**0.5
    return length
      
     
    
def polygon(x,a=9999):
    
    for i in range(x):
        t.forward(varlength(x,a))
        t.left(360/x)

for i in range(3,12):
    polygon(i)
    

turtle.done()
