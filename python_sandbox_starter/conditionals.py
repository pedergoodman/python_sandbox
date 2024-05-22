# If/ Else conditions are used to decide to do something based on something being true or false
x = 31
y = 21


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
# a colon AND an indent is needed to start the logic block of a function and a conditional statement
if x > y:
  print(f'{x} is greater than {y}')
  
# if, elif, else
if y > x:
  print(f'{y} is greater than {x}')
elif x == y:
  print(f'{x} is equal to {y}')
else:
  print(f'{y} is less than {x}')

# nested
if x > 2:
  if x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) - Used to combine conditional statements
# and
if x > 2 and x <= 40:
  print(f'{x} is greater than 2 and less than or equal to 40')

# or
if x > 2 or x <= 10:
  print(f'{x} is greater than 2 or less than or equal to 10')

# not
if not(x == y):
  print(f'{x} is not equal to {y}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
z = 3
z2 = 20

numbers = [1,2,3,4,5]

if z in numbers: # if z is in numbers, return true
  print(z in numbers)
  
if z2 not in numbers: # if z is not in numbers, return false
  print(z2 not in numbers)



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

x2 = 10 
y2 = 10


object1 = {
  'name': 'Peder',
  'age': 30,
  'city': 'Iowa City'
}

# THIS REASSIGNS THE MEMORY LOCATION OF object2 TO object1
# IF YOU CHANGE object2, object1 WILL ALSO CHANGE
# object2 = 1
object2 = object1

object2['city'] = 'Boston'

# print(object2['city'])

if x2 is y2:
  print(f'x2-y2 {x2 is y2}')
  
  
if object1 is object2:
  print(f'object1-object2 {object1 is object2}')
  print(f'object1 {object1}')
  print(f'object2 {object2}')