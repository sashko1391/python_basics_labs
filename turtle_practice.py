import turtle

screen = turtle.Screen()
screen.title('Turtle Practice')

t = turtle.Turtle()
t.speed(1)
t.color('blue')

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def polygon(sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

polygon(10, 20)
polygon(180, 2)
turtle.done()