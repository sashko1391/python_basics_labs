names = ['Igor', 'Sasha', 'maks', 'Dimarik']
print(names[0])

print(names[2].title())

print(names[-1].upper())    

print(names[1], names[3])

print(f"Hello, {names[2].capitalize()}, would you like to learn some Python today?")

guests = ['buddha', 'jesus', 'muhammad', 'krishna', 'confucius']
print(f"I would like to invite {guests[0].title()} to dinner.") 
print(f"I would like to ask {guests[1].title()}, {guests[2].title()}, {guests[3].title()} and {guests[4].title()} to join us.")
print(f"Unfortunately, {guests[-1].title()} cannot make it to dinner.")
guests[4] = 'plato'
print(f"I would like to invite {guests[0].title()} to dinner.") 
print(f"I would like to ask {guests[1].title()}, {guests[2].title()}, {guests[3].title()} and {guests[4].title()} to join us.")
print("Good news! We found a bigger dinner table.")
guests.insert(0, 'socrates')
guests.insert(3, 'aristotle')
guests.append('descartes')
print(f"I would like to invite {guests[0].title()} to dinner.") 
print(f"I would like to ask {guests[1].title()}, {guests[2].title()}, {guests[3].title()}, {guests[4].title()}, {guests[5].title()}, {guests[6].title()} and {guests[7].title()} to join us.")
print("Sorry, the new dinner table won't arrive in time. I can only invite two people for dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest.title()}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest.title()}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest.title()}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest.title()}, I can't invite you to dinner.")
print(f"{guests[0].title()}, you are still invited to dinner.")
print(f"{guests[1].title()}, you are still invited to dinner.")
del guests[1]
del guests[0]
print(guests)
guests.remove('jesus')
print(guests)
guests.remove('aristotle')
print(guests)

places_to_visit = ['japan', 'italy', 'bali', 'greece', 'switzerland']
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
print(sorted(places_to_visit, reverse=True))
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)
print(len(guests))

numbers = list(range(1, 21))
print(numbers)

numbers = list(range(1, 101))
for number in numbers:
    print(number)

min_number = min(numbers)
print(min_number)
max_number = max(numbers)
print(max_number)
sum_numbers = sum(numbers)
print(sum_numbers)

numbers = list(range(1, 21, 2))
print(numbers)

numbers = list(range(3, 31, 3))
for number in numbers:
    print(number)

cubes = [value**3 for value in range(1, 11)]
print(cubes)    

print(f"The firast three plases to visit are: {places_to_visit[:3]}")
print(f"Three places from the middle of the list are: {places_to_visit[1:4]}")
print(f"The last three places to visit are: {places_to_visit[-3:]}")    

friends_places = places_to_visit[:]
print("My favorite places are:")
print(places_to_visit)
print("My friend's favorite places are:")
print(friends_places)
places_to_visit.append('australia')
friends_places.append('spain')
print("My favorite places are:")
print(places_to_visit)
print("My friend's favorite places are:")
print(friends_places)   