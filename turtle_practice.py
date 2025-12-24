import turtle
import math

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

#polygon(10, 20)
#polygon(180, 2)

def circle(radius):
    circumference = 2 * 3.14 * radius
    sides = 100
    length = circumference / sides
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)
#circle(50)

t.clear()

def parallelogram(side_width, side_height, angle):
    for i in range(2):
        t.forward(side_width)
        t.left(angle)
        t.forward(side_height)
        t.left(180 - angle)

def rectangle(side_width, side_height):
    parallelogram(side_width, side_height, 90)

#rectangle(100, 50)
turtle.done()
t.clear()

def triangle(side_length):
    for i in range(3):
        t.forward(side_length)
        t.left(120)
triangle (60)
turtle.done()
t.clear()

def trianglepie(sides, base):
    base_angle = 360 / sides / 2
    ver_angle = 180 - (base_angle * 2)
    ver_angle_rad = math.radians(ver_angle)
    cos_ver = math.cos(ver_angle_rad)
    leg_length = base / (2 * cos_ver)
    for i in range(sides):
        t.forward(base)
        t.left(base_angle)
        t.forward(leg_length)
        t.left(ver_angle)
        t.forward(leg_length)
        t.left(base_angle)
        t.penup()
        t.forward(base)
        t.pendown()

trianglepie(6, 50)
turtle.done()
t.clear()

could yoy check my 