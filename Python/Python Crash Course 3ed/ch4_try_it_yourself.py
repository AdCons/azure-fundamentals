'''Python Crash Course 3ed - Chapter 4 - Try It Yourself'''

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store
# these pizza names in a list, and then use a for loop to print the name of
# each pizza.
# • Modify your for loop to print a sentence using the name of the pizza,
# instead of printing just the name of the pizza. For each pizza, you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!
pizzas = ["pepperoni", "mushroom", "cheese"]
for pizza in pizzas:
    print("I like", pizza, "pizza.")
print("I really love pizza!")

# 4-2. Animals: Think of at least three different animals that have a common
# characteristic. Store the names of these animals in a list, and then use a
# for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog
# would make a great pet.
# • Add a line at the end of your program, stating what these animals have in
# common. You could print a sentence, such as Any of these animals would make
# a great pet!
animals = ["dog", "cat", "rabbit"]
for animal in animals:
    print("A", animal, "would make a great pet.")
print("Any of these animals would make a great pet!")

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
for number in range(1, 21):
    print(number)

# 4-4. One Million: Make a list of the numbers from one to one million, and
# then use a for loop to print the numbers. (If the output is taking too long,
# stop it by pressing CTRL-C or by closing the output window.)
numbers = list(range(1000001))
for num in numbers:
    print(num)

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one
# and ends at one million. Also, use the sum() function to see how quickly
# Python can add a million numbers.
print("The minimum value is", min(numbers))
print("The maximum value is", max(numbers))
print("The sum of the numbers is", sum(numbers))

# 4-6. Odd Numbers: Use the third argument
# of the range() function to make a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.
odds = list(range(2, 21, 2))
for odd in odds:
    print(odd)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop
# to print the numbers in your list.
threes = list(range(3, 31, 3))
for t in threes:
    print(t)

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes
# (that is, the cube of each integer from 1 through 10), and use a for loop to
# print out the value of each cube.
cubes = []
for val in range(1, 11):
    cubes.append(val**3)

for cube in cubes:
    print(cube)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
cubes = [cube**3 for cube in range(1, 11)]

# 4-10. Slices: Using one of the programs you wrote in this chapter, add
# several lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice
# to print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a
# slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice
# to print the last three items in the list.
months = [
    "jan", "feb", "mar", "apr", "may", "jun",
    "jul", "aug", "sep", "oct", "nov", "dec"
    ]
print("The first three items in the list are:", months[:3])
print("Three items from the middle of the list are:", months[4:7])
print("The last three items in the list are:", months[:-3])

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise
# 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message
# My favorite pizzas are:, and then use a for loop to print the first list.
# Print the message My friend’s favorite pizzas are:, and then use a for loop
# to print the second list. Make sure each new pizza is stored in the
# appropriate list.
friend_pizzas = pizzas[:]
pizzas.append("hawaiian")
friend_pizzas.append("meat lovers")
for pizza in pizzas:
    print("My favorite pizzas are:", pizza)
for friends_pizza in friend_pizzas:
    print("My friend's favorite pizzas are:", friends_pizza)

# 4-12. More Loops: All versions of foods.py in this section have avoided
# using for loops when printing, to save space. Choose a version of foods.py,
# and write two for loops to print each list of foods.
dishes = ["pizza", "falafel", "carrot cake"]
for dish in dishes:
    print(dish)

# 4-14. PEP 8: Look through the original PEP 8 style guide at
# https://python.org/ dev/peps/pep-0008. You won’t use much of it now, but it
# might be interesting to skim through it.

# 4-15. Code Review: Choose three of the programs you’ve written in this
# chapter and modify each one to comply with PEP 8.
# • Use four spaces for each indentation level. Set your text editor to insert
# four spaces every time you press the TAB key, if you haven’t already done so
# (see Appendix B for instructions on how to do this).
# • Use less than 80 characters on each line, and set your editor to show a
# vertical guideline at the 80th character position.
# • Don’t use blank lines excessively in your program files.
