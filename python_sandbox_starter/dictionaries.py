# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# create dictonary

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}


# use a constructor
person2 = dict(first_name='Sara', last_name='Williams')


print(person2, type(person))
print(person2, type(person2))


#get value
print(person['first_name'])
print(person.get('last_name'))

# add key/value
person['phone'] = '555-555-5555'

print(person)
print(person.keys()) # list of keys
print(person.items()) # key value pairs, returns tuples

person2 = person.copy()
person2['city'] = 'Boston'

print(person2)



# remove item, pass in key to remove
del(person['age']) # or person.pop('age')

print(person)

# clear
person.clear() # removes everything
print(person) # {}

# get length
print(len(person2)) # 3


list_of_people = [
  {'name': 'Martha', 'age': 30},
  {'name': 'Kevin', 'age': 25},
  {'name': 'Karen', 'age': 35}
]


list_of_people2 = [
  {
    'name': {
      'first': 'Martha', 
      'last': 'Stewart'
    }, 
    'age': 30
  },
]

firstName = list_of_people2[0]['name']['first']
lastName = list_of_people2[0]['name']['last']
fullName = f'{firstName} {lastName}'

print(fullName)