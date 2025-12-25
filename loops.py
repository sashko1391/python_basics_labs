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

promt = "Please enter a number, and I'll tell you if it's even or odd: "
promt += "\nEnter 'quit' to end the program. "

while True:
    number = input(promt)
    if number == 'quit':
        break
    else:
        number = int(number)
        if number % 2 == 0:
            print(f"The number {number} is even.")
        else:
            print(f"The number {number} is odd.")


promt_2 = "Please enter the pizza topping you would like: "
promt_2 += "\nEnter 'quit' when you are finished. "

active = True
while active:

    topping = input(promt_2)
    if topping == 'quit':
        active = False
        print(f"Thank you for your order!") 
    else:
        print(f"I'll add {topping} to your pizza.")

promt_3 = "Please enter the age of the person: "
promt_3 += "\nEnter 'quit' to end the program. "

while True:
    age = input(promt_3)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("The ticket is free.")
        elif age <= 12:
            print("The ticket is $10.")
        else:
            print("The ticket is $15.")


active = True
while active:
    age = input(promt_3)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("The ticket is free.")
        elif age <= 12:
            print("The ticket is $10.")
        else:
            print("The ticket is $15.")


while True:
    topping = input(promt_2)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping.title()} to your pizza.") 

sandwich_orders = ['turkey', 'veggie', 'club', 'pastrami', 'ham', 'pastrami', 'roast beef', 'pastrami']
finished_sandwiches = []   
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("All sandwiches are made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")

print("Sorry, we have run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("All sandwiches are made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")