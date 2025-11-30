pizza = ['margherita', 'pepperoni', 'hawaiian', 'bbq chicken']
for topping in pizza:
    print(f'{topping.title()}')
    print(f"I love {topping} pizza!") 
print("I really love pizza!")

animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print(f'{animal.title()}')
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!")

friends_pizza = pizza[:]
friends_pizza.append('veggie')
print("My favorite pizzas are:")
for pizza_type in pizza:
    print(f"- {pizza_type.title()}")
print("My friend's favorite pizzas are:")
for pizza_type in friends_pizza:
    print(f"- {pizza_type.title()}")    