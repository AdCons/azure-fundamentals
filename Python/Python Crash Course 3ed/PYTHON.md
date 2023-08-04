# Python Crash Course 3rd Edition

The purpose of this book is to make you a good programmer in general and a good Python programmer in particular. You’ll learn efficiently and adopt good habits as you gain a solid foundation in general programming
concepts.

Python is an incredibly efficient language: your programs will do more in fewer lines of code than many other languages would require. Python’s syntax will also help you write “clean” code. Your code will be easier to read, easier to debug, and easier to extend and build upon, compared to other languages.

## Chapter 1: Getting Started

In this chapter, you’ll run your first Python program, ***hello_world.py***. First, you’ll need to check whether a recent version of Python is installed on your computer; if it isn’t, you’ll install it. You’ll also install a text editor to work with your Python programs. Text editors recognize Python code and highlight sections as you write, making it easy to understand your code’s structure.

Check Python version, then run ***hello_world.py***:

```bash
python --version
python hello_world.py
```

## Chapter 2: Variables and Simple Data Types

In this chapter you’ll learn about the different kinds of data you can work with in your Python programs. You’ll also learn how to use variables to represent data in your programs.

## Variables

Every ***variable*** is connected to a value, which is the information associated with that variable. Adding a variable makes a little more work for the Python interpreter.

```python
# Write a Hello World message
M = 777
print(M)
```

It’s much better to think of variables as labels that you can also say that a variable references a certain value.

A ***traceback*** is a record of where the interpreter ran into trouble when trying to execute your code. If Python finds a variable name that’s similar to the one it doesn’t recognize, it will ask if that’s the name you meant to use.

## Strings

A string is a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around your
strings like this:

```python
# Single quotes
'Hello World'
# Double quotes
"Hello World"
```

One of the simplest tasks you can do with strings is change the case of the words in a string.

A ***method*** is an action that Python can perform on a piece of data. The dot (.) after name in ***name.title()*** tells Python to make the ***title() method*** act on the variable name.

The ***lower()*** method is particularly useful for storing data. The ***upper()*** method is makes all letters uppercase. The ***title()*** method makes the first letter of each word uppercase.

```python
# Write a Hello World message
M = "hElLo WoRlD!"

print(M.title())  # Title case
print(M.upper())  # Upper case
print(M.lower())  # Lower case
```

***f-string*** is a literal string, prefixed with 'f', which contains expressions inside braces. In programming, ***whitespace*** refers to any non-printing characters, such as ***spaces, tabs, and end-of-line symbols***. The string ***"\n\t"*** tells Python to move to a new line, and start the next line with a tab.

Python can look for extra whitespace on the right and left sides of a string. To ensure that ***no whitespace exists*** at the right side of a string, use the ***rstrip()*** method. In the real world, these stripping functions are used most often to clean up user input before it’s stored in a program.

```python
# f-strings: formatting variable values to strings
FIRST_NAME = "ada"
LAST_NAME = "lovelace"
full_name = f"{FIRST_NAME} {LAST_NAME}"
print(f"No Strips:\n\tHello,   {full_name.title()}  !   ")
print(f"Strips:\n\tHello,{full_name.title()}!".strip().removeprefix("Strips:"))
```

A ***syntax error*** occurs when Python doesn’t recognize a section of your program as valid Python code. This syntax error indicates that the interpreter doesn’t recognize something in the code as valid Python code.

***Syntax errors*** are also the least specific kind of error, so they can be difficult and frustrating to identify and correct. Your editor’s syntax highlighting feature should help you spot some syntax errors quickly as you write your programs.

### Numbers

Python treats numbers in several different ways, depending on how they’re being used.

- ***Integer***: A whole number (e.g., 2, 3, 4, 5, 6, and so on).
- ***Float***: Any number with a decimal point (e.g., 2.0, 3.1, 4.2, 5.3, 6.4, and so on).

When you divide any two numbers, even if they are integers that result in a whole number, ***you’ll always get a float***. If you mix an integer and a float in any other operation, ***you’ll get a float as well***.

```python
# Arbitrary number of decimal places
print(0.2 + 0.1)
print(3 * 0.1)
```

You can assign values to ***more than one*** variable using just a single line of code. You need to separate the variable names with commas, and do the same with the values, and Python will assign each value to its respective variable.

```python
# Multiple assignments
x, y, z = 1, 2, 3
print(x, y, z)
```

When you’re writing long numbers, you can group digits using ***underscores*** to make large numbers more ***readable***. To Python, ***1000*** is the same as ***1_000***, which is the same as ***10_00***. This feature works for both integers and floats.

A ***constant*** is a variable whose ***value stays the same*** throughout the life of a program. When you want to treat a variable as a constant in your code, write the name of the variable in all capital letters.

```python
# Constants and underscores
MAX_CONNECTIONS = 5_0_0_0
print(MAX_CONNECTIONS)
```

### Comments

A comment allows you to write notes in your spoken language, within your programs. In Python, the hash mark (#) indicates a comment. Anything following a hash mark in your code is ignored by the Python interpreter. The main reason to write comments is to explain what your code is supposed to do and how you are making it work.

```python
# This is a comment. Say hello to everyone.
```

### The Zen of Python

Experienced Python programmers will encourage you to avoid complexity and aim for simplicity whenever possible.

```python
import this
```

> The Zen of Python, by Tim Peters
> Beautiful is better than ugly.

Programmers have always respected ***well-designed, efficient, and even beautiful*** solutions to problems.

> Simple is better than complex.

If you have a choice between a simple and a complex solution, and both work, ***use the simple solution***.

> Complex is better than complicated.

Real life is messy, and sometimes a simple solution to a problem is unattainable. In that case, ***use the simplest solution that works***.

> Readability counts.

Even when your code is complex, ***aim to make it readable***.

> There should be one—and preferably only one—obvious way to do it.

However, much of programming consists of using ***small, common*** approaches to simple situations within a ***larger, more creative*** project.

> Now is better than never.

***Don’t try to write perfect code; write code that works***, and then decide whether to improve your code for that project or move on to something new.

## Chapter 3: Introducing Lists

In this chapter and the next you’ll learn what lists are and how to start working with the elements in a list.

### What Is a List?

A ***list*** is a collection of items in a particular order. Because a list usually contains more than one element, it’s a good idea to make the name of your list plural, such as letters, digits, or names. In Python, ***square brackets ([])*** indicate a ***list***, and individual elements in the list are separated by commas.

```python
# A list of months
months = [
    "jan", "february", "march", "april", "may",
    "july", "august", "september", "october", "november"
    ]
```

***Lists*** are ordered collections, so you can access any element in a list by telling Python ***the position***, or index, of the item desired. Python considers ***the first item in a list to be at position 0***, not position 1. Using this counting system, you can get any element you want from a list by subtracting one from its position in the list.

If you ask for the item at ***index -1***, Python always returns the ***last item*** in the list. This syntax is quite useful, because you’ll often want to access the last items in a list ***without knowing*** exactly how long the list is.

```python
# Indexing starts at 0
print("First item is ", months[0].title(), "with Index: 0")  # "january"
# Last month: whether the list is sorted or not,
# last item index is -1 or len(list) - 1
print("Last item is ", months[-1].title(), "with Index: -1")  # "december"
```

### Modifying, Adding, and Removing Elements

Most lists you create will be dynamic, meaning you’ll build a list and then add and remove elements from it as your program runs its course. To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

```python
# Change the first month to "january"
months[0] = "january"
print(months[0].title())
```

The simplest way to ***add*** a new element to a list is to append the item to the list. The ***append()*** method makes it easy to build lists dynamically. Building lists this way is very common, because you often won’t know the data your users want to store in a program until after the program is running.

You can add a new element at any position in your list by using the ***insert()*** method. This operation shifts every other value in the list one position to the right.

```python
# Add a month to the end of the list
months.append("december")

# Add a month in any position of the list
months.insert(5, "june")

print(months[-1].title())
print(months[5].title())
```

You can remove an item from any position in a list using the del statement if you know its index.

The ***pop()*** method removes the last item in a list, but it lets you work with that item after removing it. The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. You can use ***pop()*** to remove an item from any position in a list by including the index of the item you want to remove in parentheses. Remember that each time you use ***pop()***, the item you work with is no longer stored in the list.

```python
# Remove the last month from the list
print("\nDeleting Elements:")
last_month = months.pop()  # Remove the last month from the list
print(f"The last month of the year is {last_month}")
```

When you want to delete an item from a list and not use that item in any way, use the ***del statement***; if you want to use an
item as you remove it, use the ***pop()*** method.

```python
# Remove with del statement
del months[0]  # Remove the first month from the list
```

If you only know the value of the item you want to remove, you can use the ***remove()*** method. The ***remove()*** method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a ***loop*** to make sure all occurrences of the value are removed.

```python
# Remove an item by value
print("\nRemoving Elements by Values:")
months.remove("january")  # Remove the first month from the list
print(months)
```

### Organizing a List

Python provides a number of different ways to ***organize your lists***, depending on the situation. Python’s ***sort()*** method makes it relatively easy to sort a list. The ***sort()*** method ***changes*** the order of the list permanently. You can also sort this list in ***reverse-alphabetical*** order by passing the ***argument reverse=True*** to the ***sort()*** method.

```python
# Sorting List Temporarily
print(sorted(months), "\n", sorted(months))
# Sorting a List in reverse order
print(sorted(months), "\n", sorted(months, reverse=True))
```

The ***sorted()*** function lets you display your list in a particular order, but ***doesn’t affect the actual order of the list***. The ***sorted()*** function can also accept a ***reverse=True argument*** if you want to display a list in ***reverse-alphabetical*** order.

```python
# Sorting a List Permanently: sorting months alphabetically
months.sort()

# Sorting a List in reverse order
months.sort(reverse=True)
```

To reverse the original order of a list, you can use the ***reverse()*** method. The ***reverse()*** method changes the order of a list permanently, but you can revert to the original order anytime by applying ***reverse()*** to the same list a second time. You can quickly find the length of a list by using the ***len()*** function.

```python
# Reversing Lists
months.reverse()
print(months)  # Returns a reversed iterator
```

## Chapter 4: Working with Lists

***Looping*** allows you to take the same action, or set of actions, with every item in a list.

### Looping Through an Entire List

When you want to do the same action with ***every item in a list***, you can use Python’s ***for loop***. Looping is important because it’s one of the most common ways a computer ***automates repetitive tasks***.

When you’re using loops for the first time, keep in mind that the set of steps is repeated ***once for each item in the list***, no matter how many items are in the list. Also keep in mind when writing your own ***for loops*** that you can choose any name you want for the ***temporary variable*** that will be ***associated with each value in the list***.

```python
# A list of 5 names
names = ["jose", "maria", "juan", "pedro", "luis"]

# Greet each person in the list
for name in names:
    print("Hola,", name.title(), "!")
```

Any lines of code after the for loop that ***are not indented are executed once without repetition***. When you’re processing data using a for loop, you’ll find that this is a good way to summarize an operation that was performed on an entire dataset.

### Making Numerical Lists

***Lists*** are ideal for storing sets of numbers, and Python provides a variety of tools to help you work efficiently with lists of numbers. Python’s ***range()*** function makes it easy to generate a series of numbers.The ***range()*** function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide. You can also pass ***range()*** only one argument, and it will start the sequence of numbers at 0.

```python
# A list of numbers
num_list = list(range(2, 7))
print(num_list)
```

If you want to make a list of numbers, you can convert the results of ***range()*** directly into a list using the ***list()*** function. When you wrap ***list()*** around a call to the ***range()*** function, the output will be a list of numbers. We can also use the ***range()*** function to tell Python to skip numbers in a given range. If you pass a third argument to ***range()***, Python uses that value as a step size when generating numbers.

```python
# A list of numbers
num_list = list(range(2, 7, 2))
print(num_list)
```

Sometimes using a ***temporary variable*** makes your code easier to read; other times it makes the code unnecessarily long. Focus first on ***writing code that you understand clearly***, and does what you want it to do. Then
look for ***more efficient approaches*** as you review your code.

```python
# A list of numbers
num_list = []
for x in range(2, 7):
    num_list.append(x**x)
print(num_list)
```

A ***list comprehension*** allows you to generate this same list in just ***one line of code***. A list comprehension combines the ***for loop*** and the creation of new elements into one line, and automatically ***appends each new element***.

```python
# A list of numbers
num_list = [x**x for x in range(2, 7)]
print(num_list)
```

### Working with Part of a List

You can also work with a specific group of items in a list, called a ***slice*** in Python. To make a ***slice***, you specify the index of the ***first and last*** elements you want to work with. You can generate any subset of a list.

```python
# A slice of the list
print("\nSlice of the list:", num_list[2:6])
```

If you omit the first index in a slice, Python automatically starts your slice at the ***beginning of the list***. You can include a ***third value*** in the brackets indicating a slice. If a third value is included, this tells Python how many items to ***skip between items*** in the specified range.

```python
# A slice of the 3 first items
print("\nSlice of the 3 first items:", num_list[:3])

# A slice of the 3 last items
print("\nSlice of the 3 last items:", num_list[-3:])  # Negative index

# A slice of the list 2-by-2
print("\nSlice of the list:", num_list[2:6:2], "\n")  # 2-by-2
```

You can use a slice in a ***for loop*** if you want to loop through a subset of the elements in a list. When you’re working with data, you can use slices to process your data in ***chunks*** of a specific size.

```python
# Looping through a slice
for number in num_list[2:6]:
    print("Looping through Slice:", number)
```

To ***copy a list***, you can make ***a slice that includes the entire original list*** by omitting the first index and the second index ***([:])***. This tells Python to make a slice that starts at the first item and ends with the last item, producing a ***copy*** of the entire list.

```python
# Copying a list
new_number_list = num_list[:]

# Proving that the lists are different
num_list.append(100)  # Adding a new element to the original list
print("\nNew Number List:", new_number_list)
print("Number List:", num_list)
```

If you’re trying to work with a copy of a list and you see unexpected behavior, make sure you are copying the list using a slice, as we did in the first example.

### Tuples

Lists work well for storing collections of items that can change throughout the life of a program. Python refers to values that ***cannot change*** as ***immutable***, and an immutable list is called a ***tuple***.

A ***tuple*** looks just like a list, except you use ***parentheses*** instead of square brackets. Once you define a tuple, you can access individual elements by ***using each item’s index***, just as you would for a list.

```python
# Defining a Tuple
my_tuple = (1, 2, 3, 4, 5)
```

Because we’re ***trying to alter a tuple***, which can’t be done to that type of object, Python tells us ***we can’t assign a new value*** to
an item in a tuple:

```python
# Trying to change a tuple
my_tuple[0] = 10
```

You can ***loop*** over all the values in a tuple using a ***for loop***, just as you did with a list:

```python
# Iterating through a tuple slice
print("\nIterating through a tuple slice:")
for num in my_tuple[1:4]:
    print("Tuple Element:", num)
```

Although you can’t modify a tuple, ***you can assign a new value to a variable*** that represents a tuple

```python
# Assigning a new value to a tuple
my_tuple = (10, 20, 30, 40, 50)
print("\nNew Tuple:", my_tuple)
```

When compared with lists, ***tuples are simple data structures***. Use them when you want to store a set of ***values that should not be changed*** throughout the life of a program.

### Styling Your Code

The Python style guide was written with the understanding that ***code is read more often than it is written***. Python programmers will almost always encourage you to ***write code that’s easier to read***.

***PEP 8*** recommends that you use ***four spaces*** per ***indentation level***. ***Mixing*** tabs and spaces in your file ***can cause problems*** that are very difficult to diagnose.

Many Python programmers recommend that ***each line should be less than 80 characters***. ***PEP 8*** also recommends that you ***limit all of your comments to 72 characters per line***.

You should ***use blank lines*** to organize your files, but ***don’t do so excessively***. Blank lines won’t affect how your code runs, but they will ***affect the readability*** of your code.

## Chapter 5 - If Statements

Python’s ***if statement*** allows you to examine the ***current state*** of a program and ***respond appropriately*** to that state.

### Conditional Tests

At the heart of every ***if statement*** is an expression that can be evaluated as ***True*** or ***False*** and is called a ***conditional test***. Python uses the values ***True*** and ***False*** to decide whether the code in an ***if statement*** should be executed. If a conditional test evaluates to True, Python ***executes the code following*** the ***if statement***. If the test evaluates to False, ***Python ignores the code following*** the ***if statement***.

```python
# Conditional Test
print("Conditional Test:")
print(5 == 5)
print(5 == 6)
```

This ***equality operator*** returns ***True*** if the values on the left and right side of the operator ***match***, and ***False*** if they ***don’t match***.

When you want to determine whether two values are ***not equal***, you can use the ***inequality operator (!=)***. Most of the conditional expressions you write will test for equality, but sometimes you’ll find it ***more efficient*** to test for inequality.

```python
# Inequality Operator
print("\nInequality Operator:")
print(5 != 5)
print(5 != 6)
```

***Each*** mathematical comparison can be used as part of an ***if statement***, which can help you detect the exact conditions of interest. To improve readability, you can ***use parentheses*** around the individual tests, but they are not required.

The keyword ***or*** allows you to check ***multiple conditions*** as well, but it passes when ***either or both*** of the individual tests pass.

```python
# Using the or keyword
print("\nUsing the or keyword:")
print(5 == 5 or 5 == 6)
print(5 == 5 or 5 == 5)
```

This technique is quite powerful because you can create a list of essential values, and then easily check whether the value you’re testing matches one of the values in the list.

You can use the keyword ***not***.

```python
# Using the not keyword
print("\nUsing the not keyword:")
print(not 5 == 5)
print(not 5 == 6)
```

A ***Boolean expression*** is just another name for a conditional test. A ***Boolean value*** is either ***True*** or ***False***, just like the value of a ***conditional expression*** after it has been evaluated. ***Boolean values*** provide an ***efficient way to track*** the state of a program or a particular condition that is important in your program.

### If Statements

When you understand ***conditional tests***, you can start writing ***if statements***. Several different kinds of ***if statements*** exist, and your choice of which to
use ***depends on the number of conditions*** you need to test. ***Indentation*** plays the ***same role*** in ***if statements*** as it did in ***for loops***. All indented lines after an if statement ***will be executed*** if the test passes, and the entire block of indented lines ***will be ignored*** if the test does not pass.

```python
# Numerical comparisons:
print("Numerical comparisons:")
NUM1 = -5
if NUM1 >= 0:
    print("The number is positive")
else:
    print("The number is negative")

print("\nString comparisons:")
# String comparisons:
STRING1 = ""
if STRING1:
    print("The string is not empty")
else:
    print("The string is empty")
```

An ***if-else block*** is similar to a simple ***if statement***, but the ***else statement*** allows you to define an action or set of actions that are executed ***when the conditional test fails***. Python ***executes only one block*** in an ***if-elif-else chain***. It runs each conditional test in order, ***until one passes***. When a test passes, the code following that test is executed and Python ***skips the rest*** of the tests. You can use as many ***elif blocks*** in your code as you like. Python does not require an ***else block*** at the end of an ***if-elif chain***.

```python
# if-elif-else chain
print("\nif-elif-else chain:")
AGE = 12
if AGE < 4:
    print("Your admission cost is $0.")
elif AGE < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
```

The ***else block*** is a ***catchall statement***. It matches any condition that wasn’t matched by a specific ***if or elif test***, and that can sometimes include invalid or even malicious data. If you have a specific final condition you’re testing for, consider using a final ***elif block*** and omit the ***else block***. The ***if-elif-else chain is powerful***, but it’s only appropriate to use when you just need ***one test to pass***. As soon as Python finds one test that passes, it skips the rest of the tests.

However, sometimes it’s important to ***check all conditions*** of interest. In this case, you should use a ***series of simple if statements*** with no ***elif*** or ***else*** blocks.

```python
# Multiple if statements
print("\nMultiple if statements:")
TOPPINGS = ["mushrooms", "extra cheese"]
if "mushrooms" in TOPPINGS:
    print("Adding mushrooms.")
if "pepperoni" in TOPPINGS:
    print("Adding pepperoni.")
if "extra cheese" in TOPPINGS:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
```

In summary, if you want ***only one block*** of code to run, use an ***if-elif-else chain***. If ***more than one block*** of code needs to run, use a ***series of independent if statements***.

### Using if Statements with Lists

You can do some interesting work when you combine ***lists*** and ***if statements***. You can watch for ***special values*** that need to be treated differently than other values in the list.

```python
fruits = (
    'apple', 'banana', 'orange', 'watermelon', 'pineapple', 'grape'
    )
requested_fruits = [
    'apple', 'Blueberry', 'banana', 'strawberry', 'watermelon',
    'raspberry', 'grape', 'kiwi'
    ]

# Checking if list values are in other list:
print("\nChecking if list values are in other list:")
for req_fruit in requested_fruits:
    if req_fruit in fruits:
        print(f"Adding {req_fruit} to the basket")
    else:
        print(f"{req_fruit} is not available")
```

In this situation, it’s useful to check whether a list is ***empty*** before running a for loop. When the name of a list is used in an ***if statement***, Python returns ***True*** if the list contains at least one item; an empty list evaluates to ***False***.

```python
# Checking if list is empty:
print("\nChecking if list is empty:")
requested_fruits = []
if requested_fruits:
    for req_fruit in requested_fruits:
        if req_fruit in fruits:
            print(f"Adding {req_fruit} to the basket")
        else:
            print(f"{req_fruit} is not available")
else:
    print("The basket is empty")
```

The only recommendation ***PEP 8*** provides for styling conditional tests is to use a ***single space*** around comparison operators, such as ***==, >=, and <=***.

## Chapter 6 - Dictionaries

Understanding ***dictionaries*** allows you to model a variety of real-world objects more accurately.

### Working with Dictionaries

A ***dictionary*** in Python is a collection of ***key-value pairs***. A ***key’s value*** can be a ***number, a string, a list, or even another dictionary***.

A ***key-value pair*** is a set of values associated with each other. When you provide a ***key***, Python returns the ***value*** associated with that ***key***. Every ***key*** is connected to its value by a ***colon***, and individual ***key-value pairs*** are separated by commas.

```python
# A Knight is a character in a game with the following attributes:
knight = {
    'hp': '100',
    'mana': '50',
    'helmet': 'royal helmet',
    'helmet2': 'royal helmet',
    }

# A Wizard is a character in a game with the following attributes:
wizard = {
    'hp': '50',
    'mana': '150',
    'weapon': 'death wand',
    'shield': 'spellbook',
    'helmet': "Rabadon's deathcap",
    }

# A Paladin is a character in a game with the following attributes:
paladin = {
    'hp': '75',
    'mana': '75',
    'weapon': 'arbalest',
    'shield': 'light shield',
    'helmet': 'skull helmet',
    }

# Access to a dictionary value:
print("\nAccess to a dictionary value:")
print(f"Knight's helmet: {knight['helmet']}")
print(f"Wizard's weapon: {wizard['weapon']}")
print(f"Paladin's shield: {paladin['shield']}")
```

***Dictionaries*** are ***dynamic structures***, and you can add ***new key-value pairs*** to a dictionary at any time. To add a ***new key-value pair***, you would give the ***name of the dictionary*** followed by the ***new key*** in square brackets, along with the ***new value***.

```python
# Adding new attributes to a dictionary:
print("\nAdding new attributes to a dictionary:")
knight['shield'] = 'blessed shield'
knight['weapon'] = 'fire axe'
print(f"Knight's armor: {knight['weapon']}")
print(f"Knight's shield: {knight['shield']}")
```

***Dictionaries*** retain the ***order*** in which they were defined.

To start filling an ***empty dictionary***, define a dictionary with an ***empty set of braces*** and then add each key-value pair on its own line.

```python
    # Starting with an empty dictionary:
    print("\nStarting with an empty dictionary:")
    druid = {}
    druid['hp'] = '75'
    druid['mana'] = '75'
    druid['weapon'] = 'wand'
```

To ***modify*** a value in a dictionary, give the name of the dictionary with the key in square brackets and then the ***new value*** you want associated with that key.

```python
# Change value of an attribute in dictionary:
print("\nChange value of an attribute in dictionary:")
knight['shield'] = 'dragon scale shield'
knight['weapon'] = 'ice hammer'
print(f"Knight's new shield: {knight['shield']}")
print(f"Knight's new weapon: {knight['weapon']}")
```

When you no longer need a piece of information that’s stored in a dictionary, you can use the ***del statement***  to completely ***remove a key-value pair*** .

```python
# Deleting an attribute from a dictionary:
print("\nDeleting an attribute from a dictionary:")
del knight['helmet2']
# returns "no helmet" if key "helmet" does not exist
print(f"Knight's helmet: {knight.get('helmet', 'no helmet')}")
```

Be aware that the deleted key-value pair is ***removed permanently***.

For dictionaries specifically, you can use the ***get() method*** to set a default value that will be returned if the ***requested key doesn’t exist***.

```python
# Using get() method to set a default value:
print("\nUsing get() method to set a default value:")
print(f"Knight's helmet: {knight.get('helmet', 'no helmet')}")
print(f"Wizard's helmet: {wizard.get('helmet', 'no helmet')}")
print(f"Paladin's helmet: {paladin.get('helmet', 'no helmet')}")
```

If you leave out the second argument in the call to ***get()*** and the key doesn’t exist, Python will return the value ***None***.

### Looping Through a Dictionary

You can ***loop*** through all of a ***dictionary’s key-value pairs***, through its ***keys***, or through its ***values***. To write a ***for loop*** for a dictionary, you create names for the two variables that will hold the ***key and value*** in each key-value pair.

```python
# Looping through all key-value pairs:
print("\nLooping through all key-value pairs:")
for attribute, value in knight.items():
    print(f"Attribute: {attribute} Value: {value}")
```

The ***keys() method*** is useful when you don’t need to work with all of the values in a dictionary.

```python
# Looping through all keys:
print("\nLooping through all keys:")
for attribute in knight:
    print(f"Attribute: {attribute}")
```

If you are primarily interested in the ***values*** that a dictionary contains, you can use the ***values() method*** to return a sequence of values without any keys.

```python
# Looping through all values:
print("\nLooping through all values:")
for value in knight.values():
    print(f"Value: {value}")
```

When you wrap ***set()*** around a collection of values that contains ***duplicate items***, Python identifies the ***unique items*** in the collection and builds a ***set*** from those items.

```python
# Looping through non repetitive iterator(values):
print("\nLooping through non repetitive iterator(values):")
for values in sorted(set(knight.values())):
    print(f"Value: {values}")
```

You can build a ***set*** directly using braces and separating the elements with commas:

```python
# Building a set directly:
print("\nBuilding a set directly:")
weapons = {'fire axe', 'ice hammer', 'arbalest', 'death wand'}
print(f"Weapons: {weapons}")
```

### Nesting

You can ***nest*** dictionaries inside a ***list***, a list of items inside a dictionary, or even a dictionary inside another ***dictionary***.

```python
# Creating a list of dictionaries and duplicate each character hp and mana:
print("\nCreating a list of dictionaries and x2 each character hp and mana:")
team = [knight, wizard, paladin]
# Adding more hp and mana to each character:
for character in team:
    character['hp'] = str(int(character['hp']) * 2)
    character['mana'] = str(int(character['mana']) * 2)
    print(character)
```

You can nest a ***dictionary inside another dictionary***, but your code can get complicated quickly when you do.

```python
# Dictionaries inside dictionaries:
print("\nDictionaries inside dictionaries:")
knight = {
    'hp': '100',
    'mana': '50',
    'helmet': 'royal helmet',
    'weapon': {
        'name': 'serpent sword',
        'atk': '50',
        'def': '30',
        'weight': '50.00 oz',
        },
    'shield': {
        'name': 'thorn shield',
        'atk': '0',
        'def': '60',
        'weight': '60.00 oz',
        },
    }

# Looping through nested dictionaries:
print("\nLooping through nested dictionaries:")
for attribute, value in knight.items():
    if isinstance(value, dict):
        print(f"\n{attribute.title()}:")
        for stat in value:
            print(f"\t{stat.title()}: {value[stat]}")
    else:
        print(f"\n{attribute.title()}: \n\t{value}")
```

## Chapter 7 - User Input and While Loops

### How the input() Function Works

The ***input() function*** pauses your program and waits for the user to ***enter some text***. The ***input() function*** takes one argument: the prompt that we want to ***display*** to the user, so they know what kind of information to enter.

```python
# An Python User Input is a way to get information from the user.
num_people = int(input("How many people are in your dinner group? "))

if num_people > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready. Please follow me.")
```

When you use the ***input() function***, Python interprets everything the user enters as a ***string***.

A useful tool for working with numerical information is the ***modulo operator (%)***, which divides one number by another number and returns the ***remainder***:

```python
# Modulo operator:
number = int(input("Is this number a multiple of 10?: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
```

When one number is ***divisible*** by another number, the ***remainder is 0***, so the modulo operator always ***returns 0***.

### Introducing while Loops

The ***for loop*** takes a collection of items and executes a block of code once ***for each item in*** the collection. In contrast, the while loop runs as long as, or while, ***a certain condition is true***.

```python
# Using a while loop:
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

For a program that should run only as long as ***many conditions*** are ***true***, you can define one ***variable*** that determines whether or not the entire program is ***active***. This variable, called a ***flag***, acts as a signal to the program.

```python
# A Flag is a variable that determines when a program should stop running.
FLAG = True
while FLAG:
    number = int(input("Is this number a multiple of 10?: "))
    if number % 10 == 0:
        print(f"{number} is a multiple of 10.")
        FLAG = False
    else:
        print(f"{number} is not a multiple of 10.")
```

To exit a ***while loop*** immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the ***break statement***.

Rather than ***breaking out*** of a loop entirely without executing the rest of its code, you can use the ***continue statement*** to return to the ***beginning of the loop***, based on the result of a conditional test.

```python
# Break statements can be used to exit a loop.
# Continue statements can be used to skip over certain parts of a loop.
list_random_words = ["cat", "dog", "bird", "fish", "horse", "snake", "mouse"]
X = 0
FLAG = True
while FLAG:  # active flag. Ends after entering 3 words in list.
    word = input("Enter a word: ")
    if word == "quit":
        print("Goodbye!")
        break  # break statement. Ends if "quit" is entered.
    if word not in list_random_words:
        print(f"{word} is not in the list.")
        continue  # continue statement. Avoid printing "is in the list".
    print(f"{word} is in the list.")
    if X >= 3:  # active variable. Flag turns false after 3 words entered.
        FLAG = False
    else:
        X += 1
```

### Using a while Loop with Lists and Dictionaries

A ***for loop*** is effective for looping through a list, but you ***shouldn’t modify*** a list inside a ***for loop*** because Python will have trouble keeping track of the items in the list. To modify a list as you work through it, use a ***while loop***. Using ***while loops*** with ***lists and dictionaries*** allows you to collect, store, and organize lots of input to examine and report on later.

```python
# Moving Items from One List to Another
sandwich_orders = ["tuna", "pastrami", "ham", "pastrami", "turkey", "pastrami"]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")

# Removing All Instances of Specific Values from a List
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Filling a Dictionary with User Input
responses = {}
ACTIVE = True
while ACTIVE:
    name = input("\nWhat is your name?: ")
    response = input("If you could visit one place in the world, where would you go?: ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no): ")
    if repeat == 'no':
        ACTIVE = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")
```

## Chapter 8 - Functions

When you want to perform a particular task that you’ve
defined in a ***function***, you call the ***function*** responsible for it. If you need to perform that task multiple times throughout your program, you don’t need to ***type all*** the code for the same task again and again.

### Defining a Function

The first line uses the ***keyword def*** to inform Python that you’re ***defining a function***. The text on the second line is a comment called a ***docstring***, which describes what the function does.

```python
# A function is a block of code that performs a specific task.
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
```

To call a function, you ***write*** the name of the function, followed by any necessary information in ***parentheses***.

```python
# A function call tells Python to execute the code in the function.
greet_user()
```

A ***variable*** in the function definition is a ***parameter***, a piece of information the function ***needs*** to do its job. An ***argument*** is a piece of information that’s passed from a ***function call*** to a function.

```python
# A parameter is a piece of information the function needs to do its job.
# An argument is a piece of information that’s passed from a function call to a function.
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user('jesse')
```

### Passing Arguments

Because a function definition can have ***multiple parameters***, a function call may need ***multiple arguments***.

You can use ***positional arguments***, which need to be in the same order the parameters were written. ***Keyword arguments***, where each argument consists of a ***variable name and a value***.

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# A positional argument is a piece of information that’s passed from a function call to a function.
describe_pet('hamster', 'harry')

# A keyword argument is a name-value pair that you pass to a function.
describe_pet(animal_type='hamster', pet_name='harry')
```

When you define a ***default value*** for a parameter, you can exclude the ***corresponding argument*** you’d usually write in the function call.

```python
# A default value is a value that’s assumed by a function parameter if a value isn’t provided in the function call.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
```

Using ***default values*** can simplify your function calls and clarify the ways your functions are typically used.

### Return Values

The value the function returns is called a ***return value***. The ***return statement*** takes a value from inside a function and sends it back to the line that called the function.

```python
# Returning a simple value.
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Making an argument optional.
def get_formatted_name(first_name, last_name, middle_name=''):
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
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

### Passing a List

You’ll often find it useful to pass a ***list*** to a ***function***, whether it’s a list of names, numbers, or more complex objects, such as ***dictionaries***.

When you pass a list to a function, the function can ***modify*** the list. Any ***changes*** made to the list inside the function’s body are ***permanent***, allowing you to work efficiently even when you’re dealing with large amounts of data.

```python
# Passing and modifying a list.
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
```

> If you’re writing a function and notice the function is doing too many different tasks, try to split the code into two functions.

Sometimes you’ll want to ***prevent*** a function from ***modifying*** a list. The ***slice notation [:]*** makes a copy of the list to send to the function.

```python
# Preventing a function from modifying a list.
print_models(unprinted_designs[:], completed_models)
```

> You should pass the original list to functions unless you have a specific reason to pass a copy.

### Passing an Arbitrary Number of Arguments

Python allows a function to collect an ***arbitrary*** number of ***arguments*** from the calling statement. The ***asterisk*** in the parameter name tells Python to make a ***tuple***, containing ***all the values*** this function receives.

```python
# Collecting an arbitrary number of arguments.
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    for topping in toppings:
        print(toppings)

make_pizza('pepperoni', 'green peppers', 'extra cheese')
```

This syntax works no matter how many arguments the function receives.

> The parameter that accepts an arbitrary number of arguments must be placed last in the function definition.

The ***double asterisks*** before the parameter cause Python to create a ***dictionary*** containing all the extra ***name-value pairs*** the function receives. Within the function, you can access the ***key-value*** pairs just as you would for any ***dictionary***.

```python
# Collecting an arbitrary number of keyword arguments.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
```

> The function will work no matter how many additional key-value pairs are provided in the function call.

You can mix ***positional, keyword, and arbitrary*** values in many different ways when writing your own functions.

### Storing Your Functions in Modules

Storing your ***functions*** in a ***separate file*** allows you to hide the details of your program’s code and focus on its higher-level logic. It also allows you to ***reuse functions*** in many different programs.

A ***module*** is a file ending in ***.py*** that contains the code you want to import into your program. An ***import statement*** tells Python to make the code in a module ***available*** in the currently running program file.

```python
# Importing an entire module.
import pizza

# Importing specific functions.
from module_name import function_name

# Importing specific functions.
from module_name import function_0, function_1, function_2

# Giving a function an alias.
from module_name import function_name as fn

# Giving a module an alias.
import module_name as mn

# Importing all functions in a module.
from module_name import *

pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

The ***best*** approach is to import the function or functions you want, or import the entire module and use the ***dot notation***.
