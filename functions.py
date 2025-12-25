def make_shirt(size, message):
    """Display a shirt size and message."""
    print(f"\nMaking a shirt of size {size} with the message: '{message}'")

make_shirt('L', 'Hello, World!')
make_shirt(size='M', message='Python is awesome!')

def make_shirt_default(message='I love Python', size='L'):
    """Display a shirt size and message with default size."""
    print(f"\nMaking a shirt of size {size} with the message: '{message}'")
make_shirt_default()
make_shirt_default(message='Custom message here', size='M')    

def describe_city(city, country='USA'):
    """Display the city and its country."""
    print(f"\n{city.title()} is in {country.title()}.")
describe_city('New York')
describe_city('Los Angeles')
describe_city('Tokyo', 'Japan')  

