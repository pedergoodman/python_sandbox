# A List is a collection which is ordered and changeable. Allows duplicate members.

# create a list
# more common way to create
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']


# use a constructor
# numbers2 = list((1, 2, 3, 4, 5))


# get a value
print(fruits[1]) # Oranges

# get length
print(len(fruits)) # 4


# append to list
fruits.append('Mangoes')
print(fruits) # ['Apples', 'Oranges', 'Grapes', 'Pears', 'Mangoes']

# remove from list
fruits.remove('Grapes')
print(fruits) # ['Apples', 'Oranges', 'Pears', 'Mangoes']

# insert into position
# (position, value)
fruits.insert(2, 'Strawberries')
print(fruits) # ['Apples', 'Oranges', 'Strawberries', 'Pears', 'Mangoes']

#remove from position with pop
fruits.pop(2)
print(fruits) # ['Apples', 'Oranges', 'Pears', 'Mangoes']

# reverse list order
fruits.reverse()
print(fruits) # ['Mangoes', 'Pears', 'Oranges', 'Apples']

# sort list alphabetically
fruits.sort()
print(fruits) # ['Apples', 'Mangoes', 'Oranges', 'Pears']

# reverse sort list alphabetically
fruits.sort(reverse=True)

# change value
fruits[0] = 'Blueberries'

