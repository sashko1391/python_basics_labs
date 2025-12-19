tasks = ['read chapter 4', 'practice zsh commands', 'write python loop']
tasks.append('configure codespaces')
tasks.remove('practice zsh commands')

user_profile = {
    'username': ['dev_student'],
    'current_chapter': [4],
    'is_ready_for_functions': [False]
}

user_profile['is_ready_for_functions'] = True

print(tasks)
print(user_profile)

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