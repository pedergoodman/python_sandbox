# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# * you don't need to add a "const or let" keyword to declare a variable

# * main types of variables
# x =1 # int
# y = 2.5 # float
# name = 'John' # string
# isCool = True # bool

# * Multiple assignment
x, y, name, cool = (1, 2.5, 'John', True)

print(x, y, name, cool)

xType = type(x)
xString = str(x)

print(xType)
print(xString)
print(int(y))