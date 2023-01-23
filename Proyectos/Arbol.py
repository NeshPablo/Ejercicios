from turtle import *
import random

speed(0)
bgcolor('black')
shape('turtle')
pensize(2)
pencolor('green')
left(90)
backward(100)


def tree(i):
    if i < 13:
        return
    else:
        forward(i)
        c = random.randint(1, 255)
        b = random.randint(1, 255)
        a = random.randint(1, 255)
        colormode(255)
        pencolor(c, a, b)
        circle(2)
        color('brown')
        left(30)
        tree(3*i/4)
        right(60)
        tree(3*i/4)
        left(30)
        backward(i)

def marco(a):
    if a < 10:
        return
    else:
        forward(a)
        r = random.randint(1, 255)
        b = random.randint(1, 255)
        g = random.randint(1, 255)
        colormode(255)
        pencolor(r, g, b)
        circle(2)
        color('brown')
        left(30)
        marco(3*a/4)
        right(60)
        marco(3*a/4)
        left(30)
        backward(a)

tree(80)
marco(100)
fillcolor('white')
backward(10)
pencolor('white')
right(90)
forward(20)
for i in range(36):
    left(10)
    forward(40)
backward(20)
right(90)
forward(20)
left(90)
forward(20)
for i in range(36):
    left(10)
    forward(40)
end_fill()




mainloop()
