'''Python Crash Course 3ed - Chapter 8 - Try It Yourself'''

# 8-1. Message: Write a function called display_message() that prints one
# sentence telling everyone what you are learning about in this chapter.
# Call the function, and make sure the message displays correctly.


def display_message():
    """Display a message about what I'm learning."""
    print("I'm learning to store code in functions.")


display_message()
# 8-2. Favorite Book: Write a function called favorite_book() that accepts
# one parameter, title. The function should print a message, such as One of
# my favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.


def favorite_book(title1):
    """Display a message about someone's favorite book."""
    print(f"One of my favorite books is {title1.title()}.")


favorite_book('the lord of the rings')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and
# the text of a message that should be printed on the shirt. The function
# should print a sentence summarizing the size of the shirt and the message
# printed on it. Call the function once using positional arguments to make a
# shirt. Call the function a second time using keyword arguments.


def make_shirt(size, message):
    """Display information about making a shirt."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')


make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')
# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and
# a medium shirt with the default message, and a shirt of any size with a
# different message.


def make_large_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')


make_large_shirt()
make_large_shirt(size='medium')
make_large_shirt('small', 'Programmers are loopy.')
# 8-5. Cities: Write a function called describe_city() that accepts the name
# of a city and its country. The function should print a simple sentence, such
# as Reykjavik is in Iceland. Give the parameter for the country a default
# value. Call your function for three different cities, at least one of which
# is not in the default country.


def describe_city(city='Mazatlan', country='Mexico'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)


describe_city()
describe_city('guadalajara')
describe_city('reykjavik', 'iceland')
describe_city(country='united states', city='chicago')

# 8-6. City Names: Write a function called city_country() that takes in the
# name of a city and its country. The function should return a string
# formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.


def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"


print(city_country('santiago', 'chile'))
print(city_country('sinaloa', 'mexico'))
print(city_country('paris', 'france'))

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces
# of information. Use the function to make three dictionaries representing
# different albums. Print each return value to show that the dictionaries are
# storing the album information correctly. Use None to add an optional
# parameter to make_album() that allows you to store the number of songs on an
# album. If the calling line includes a value for the number of songs, add
# that value to the album’s dictionary. Make at least one new function call
# that includes the number of songs on an album.


def make_album(artistx, titlex, songs_num=None):
    '''Collects data about an album'''
    if songs_num:
        album1 = {
            'artist': artistx,
            'title': titlex,
            'songs': songs_num
        }
    else:
        album1 = {
            'artist': artistx,
            'title': titlex
        }
    return album1


print(make_album('linkin park', 'in the end'))
print(make_album('pxndx', 'arroz con leche', 10))
# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have
# that information, call make_album() with the user’s input and print the
# dictionary that’s created. Be sure to include a quit value in the while
# loop.
while True:
    print("\nPlease tell me the artist and album title:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)

# 8-9. Messages: Make a list containing a series of short text messages. Pass
# the list to a function called show_messages(), which prints each text
# message.


def show_messages(messages):
    """Print all messages in the list."""
    for message in messages:
        print(message)


show_messages(['hello there', 'how are you?', 'what are you doing?'])
# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages
# were moved correctly.


def send_messages(messages, sent_messages):
    """
    Print each message, then move it to sent_messages.
    """
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


send_messages(['hello there', 'how are you?', 'what are you doing?'], [])
# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling
# the function, print both of your lists to show that the original list has
# retained its messages.
mess = ['hello there', 'how are you?', 'what are you doing?']
send_messages(mess[:], [])

# 8-12. Sandwiches: Write a function that accepts a list of items a person
# wants on a sandwich. The function should have one parameter that collects as
# many items as the function call provides, and it should print a summary of
# the sandwich that’s being ordered. Call the function three times, using a
# different number of arguments each time.


def sandwich(*items):
    """Summarize the sandwich we are about to make."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")


sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
sandwich('turkey', 'apple slices', 'honey mustard')
sandwich('peanut butter', 'strawberry jam')
# 8-13. User Profile: Start with a copy of user_profile.py from page 148.
# Build a profile of yourself by calling build_profile(), using your first and
# last names and three other key-value pairs that describe you.


def user_profile(first, last, **user_info):
    """Build a user's profile dictionary."""
    user_info = {
        'fist_name': first,
        'last_name': last,
    }
    return user_info


user_profile('jose', 'garcia', location='mexico', field='computer science')
# 8-14. Cars: Write a function that stores information about a car in a
# dictionary. The function should always receive a manufacturer and a model
# name. It should then accept an arbitrary number of keyword arguments. Call
# the function with the required information and two other name-value pairs,
# such as a color or an optional feature. Your function should work for a call
# like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.


def make_car(manufacturer, models, **kwargs):
    '''Store information about a car in a dictionary'''
    kwargs = {
        'manufactures': manufacturer,
        'models': models
    }
    return kwargs


make_car('subaru', 'outback', color='blue', tow_package=True)

# 8-15. Printing Models: Put the functions for the example printing_models.py
# in a separate file called printing_functions.py. Write an import statement
# at the top of printing_models.py, and modify the file to use the imported
# functions.
# 8-16. Imports: Using a program you wrote that has one function in it, store
# that function in a separate file. Import the function into your main program
# file, and call the function using each of these approaches:
# 8-17. Styling Functions: Choose any three programs you wrote for this
# chapter, and make sure they follow the styling guidelines described in this
# section.
