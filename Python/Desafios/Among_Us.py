from turtle import *
import random

title('Among US')
bgcolor('black')

color('grey')
shape('turtle')
pensize(3)
# right(50)
# fillcolor('darkblue')
# begin_fill()
left(180)
penup()
forward(50)
pendown()

right(90)
forward(100)
backward(200)
right(180)
for i in range(6):
    left(30)
    forward(20)
forward(20)
right(100)
for i in range(3):
    left(5)
    forward(20)
backward(20)
right(100)
forward(20)
for i in range(6):
    forward(20)
    left(30)
for i in range(3):
    forward(60)
    left(5)
left(90)
# end_fill()
# fillcolor('darkred')
# begin_fill()
for i in range(5):
    forward(10)
    right(5)
for i in range(15):
    forward(10)
    right(10)
right(15)
forward(50)
for i in range(16):
    right(10.1)
    forward(10)
# end_fill()
penup()
right(108)
forward(110)
pendown()
forward(10)
for i in range(3):
    left(10)
    forward(10)
for i in range(10):
    left(5)
    forward(4)
for i in range(10):
    left(2)
    forward(10)
for i in range(8):
    left(10)
    forward(10)
forward(80)
backward(20)
right(90)

fillcolor('darkblue')
begin_fill()
forward(5)
for i in range(8):
    left(10)
    forward(5)
forward(50)
for i in range(8):
    left(10)
    forward(5)
forward(19)
end_fill()
right(70)
forward(80)
right(90)

for i in range(8):
    left(10)
    forward(8)
for i in range(8):
    left(12)
    forward(13)
right(8)
for i in range(10):
    left(2)
    forward(15)
for i in range(8):
    left(12)
    forward(13)
for i in range(5):
    left(10)
    forward(8)
left(25)
penup()
forward(75)
pendown()
forward(38)
end_fill()
penup()
home()
pendown()
penup()
left(90)
forward(245)
right(90)
pendown()
fillcolor('gold')
begin_fill()
for i in range(2):
    left(5)
    forward(25)
left(90)
forward(2)
for i in range(2):
    left(5)
    forward(25)
left(130)
forward(30)
right(115)
forward(50)
left(130)
forward(50)
right(115)
forward(30)
left(130)
for i in range(2):
    left(5)
    forward(25)
forward(3)
left(90)
for i in range(2):
    left(5)
    forward(25)
end_fill()
penup()
backward(200)
pendown()

mainloop()