# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting

# Arguments by position
  # the long form way to do this
print('My name is {name} and I am {age}'.format(name=name, age=age))

  # f-strings available on python 3.6 and above
print(f'Hello, my name is {name} and I am {age}')


# String Methods
s = 'hello world'
S = s.capitalize()

print(s.capitalize()) # Capitalize first letter
print(s.upper()) # Make all uppercase
print(s.lower()) # Make all lowercase
print(S.swapcase()) # Swap case
print(len(s)) # Get string length
print(s.replace('world', 'everyone')) # Replace substring
print(s.count('l')) # Count the number of substrings, in this case the number of 'l's
print(s.startswith('hello')) # Starts with, returns boolean
print(s.endswith('d')) # Ends with returns boolean
print(s.split()) # Split string into a list (split by whitespace by default, gives you all the words in a list)
print(s.find('r')) # Find position of a substring
print(s.isalnum()) # Check if all alphanumeric, returns boolean
print(s.isalpha()) # Check if all alphabetic, returns boolean
print(s.isnumeric()) # Check if all numeric, returns boolean
