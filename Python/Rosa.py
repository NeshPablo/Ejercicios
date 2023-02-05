import turtle


def rose(turtle, size):
    for i in range(20):
        turtle.forward(size)
        turtle.right(145)
        size = size * 1.02


window = turtle.Screen()
window.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.color("red")

rose(t, 100)

turtle.done()
