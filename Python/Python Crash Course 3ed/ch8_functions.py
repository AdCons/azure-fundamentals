""" Python Crash Course - Chapter 8 - Functions """


# A function is a block of code that performs a specific task.
def greet_user1():
    """Display a simple greeting."""
    print("Hello!")


# A function call tells Python to execute the code in the function.
greet_user1()


# A parameter is a piece of information the function needs to do its job.
# An argument is a piece of information that’s passed from a function call to
# a function.
def greet_user2(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user2('jesse')


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# A positional argument is a piece of information that’s passed from a
# function call to a function.
describe_pet('hamster', 'harry')

# A keyword argument is a name-value pair that you pass to a function.
describe_pet(animal_type='hamster', pet_name='harry')


# A default value is a value that’s assumed by a function parameter if a value
# isn’t provided in the function call.
def describe_pet2(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet2(pet_name='willie')


# Returning a simple value.
def get_formatted_name1(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# Making an argument optional.
def get_formatted_name2(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted. Optional middle name."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


# Returning a dictionary.
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person


# Using a function with a while loop.
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name1(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


# Modifying a list in a function.
unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
printed = []
print_models(unprinted, printed)

# Preventing a function from modifying a list.
unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
printed = []
print_models(unprinted[:], printed)


# Collecting an arbitrary number of arguments.
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    for topping in toppings:
        print(topping)


make_pizza('pepperoni', 'green peppers', 'extra cheese')


# Collecting an arbitrary number of keyword arguments.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton',
                             field='physics')
