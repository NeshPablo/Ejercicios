#corazon con python usando la libreria turtle

from turtle import*
import random
bgcolor('black')
"""
def corazon():
    forward(10)
    right(310)
    forward(50)
    right(50)
    forward(5)
    for i in range(5):
        forward(40)
        right(30)
    right(-5)
    forward(143)
    right(75)
    forward(143)
    right(30)
    for i in range(5):
        forward(40)
        right(30)
    
    right(-100)
    forward(50)
    right(5)
    forward(50)
    clone().clone
"""
color('purple')
shape('turtle')
fillcolor('red')
begin_fill()
def corazon():
    pensize(5)
    right(-50)
    for i in range(6):
        forward(30)
        right(30)
    forward(5)
    right(10)
    forward(133)
    penup()
    home()
    pendown()
    right(50)
    for i in range(6):
        forward(-30)
        right(-30)
    right(190)
    forward(8)
    right(-20)
    forward(133)
    end_fill()
       
corazon()
mainloop()