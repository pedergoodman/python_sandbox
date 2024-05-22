# Python has functions for creating, reading, updating, and deleting files.

#open a file

# open creates a file
# 'w' is for write
# 'r' is for read
# 'a' is for append
# 'r+' is for read and write
# 'w+' is for writing and reading
myfile = open('myfile.txt', 'w')

# get some info
print('Name:', myfile.name)
print('Readable:', myfile.readable())
print('Is Closed:', myfile.closed)
print('Opening Mode:', myfile.mode)

# write to file
myfile.write('I love Python')
myfile.write(' and Javascript')
myfile.close()

print('Is Closed:', myfile.closed)


# append to file
# a is for append
myfile = open('myfile.txt', 'a')
myfile.write('\nI also like Typescript')
myfile.close()

# read from file
# r+ is for read and write
myfile = open('myfile.txt', 'r+')
text = myfile.read(100) # read first 100 characters
print(text)
