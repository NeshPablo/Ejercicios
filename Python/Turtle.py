from turtle import *
import random
import turtle

# pencolor('white')
title('jugando')
bgcolor('black')
# speed(5.5)
# forward(100)
# right(90)
# forward(200)
# left(90)
# forward(100)
# backward(50)

# circle(60)
"""
speed(0)
x = 1
while x<400:
    forward(5 + x)
    right(91)
    x+=1
#################################3
fillcolor('red')
begin_fill()
for i in range(4):
    forward(100)
    right(90)

end_fill()
"""


"""
speed(0)
pensize(5)
pencolor('white')
circle(150)
pensize(0)
x = 1
while x < 400:
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colormode(255)
    pencolor(r,g,b)
    forward(5 + x)
    right(170)
    x += 1
######################################################
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
########################################################

speed(0)
pensize(5)
pencolor('white')
circle(150)
forward(200)
pensize(0)
x = 1
while x < 400:
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colormode(255)
    pencolor(r,g,b)
    forward(5 + x)
    pencolor('white')
    circle(0.01 * x)
    right(170)
    x += 1
##########################
pencolor('white')
def estrella(longitud):
    for i in range(5):
        forward(longitud)
        right(180 - 36)


def espiral_estrellas():
    for i in range(72):
        # Estrella de 300 de longitud
        estrella(300)
        # Girar 5 grados
        right(5)


# Yo no quiero animaciones
speed(0)
# Dibujar espiral
espiral_estrellas()

"""
t = turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(2)
t.color('green')
t.left(90)
t.backward(100)
t.speed(0)
t.shape('turtle')
def tree(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color("orange")
        t.circle(2)
        t.color('brown')
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)
tree(100)
turtle.done()




mainloop()
