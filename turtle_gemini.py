import turtle
import math

t = turtle.Turtle()
t.speed(5)

def trianglepie(sides, base):
    # Кут у центрі (360 розділити на кількість шматочків)
    central_angle = 360 / sides
    # Кут при основі рівнобедреного трикутника
    base_angle = (180 - central_angle) / 2
    
    # Розрахунок довжини бічної сторони (leg)
    leg_length = (base / 2) / math.cos(math.radians(base_angle))
    
    for i in range(sides):
        # 1. Йдемо від центру до краю
        t.forward(leg_length)
        
        # 2. Малюємо зовнішню сторону (base)
        t.left(180 - base_angle)
        t.forward(base)
        
        # 3. Повертаємось назад у центр
        t.left(180 - base_angle)
        t.forward(leg_length)
        
        # 4. ГОЛОВНИЙ СЕКРЕТ: Розвертаємось на 180 (щоб знову дивитись назовні) 
        # і додаємо центральний кут для наступного шматочка
        t.left(180 + central_angle)

# Спробуй запустити це
trianglepie(6, 100)
turtle.done()