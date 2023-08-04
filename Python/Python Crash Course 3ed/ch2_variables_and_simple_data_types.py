""" Python Crash Course - Chapter 2 - Working with Lists """

# f-strings: formatting variable values to strings
FIRST_NAME = "ada"
LAST_NAME = "lovelace"
full_name = f"{FIRST_NAME} {LAST_NAME}"
print(f"No Strips:\n\tHello,   {full_name.title()}  !   ")
print(f"Strips:\n\tHello,{full_name.title()}!".strip().removeprefix("Strips:"))

# Numbers
# Arbitrary number of decimal places
print(0.2 + 0.1)
print(3 * 0.1)

# Multiple assignments
x, y, z = 1, 2, 3
print(x, y, z)

# Constants and underscores
MAX_CONNECTIONS = 5_0_0_0
print(MAX_CONNECTIONS)

# The Zen Of Python is a collection of 19 guiding principles for
# writing computer programs that influence the design of the
# Python Programming Language.
# It is written as a poem, and is included in the Python interpreter
# as an Easter Egg.

# Zen of Python
# import this  # Unused import
