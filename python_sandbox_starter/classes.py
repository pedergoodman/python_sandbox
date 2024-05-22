# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create class

class User:
  # constructor
  def __init__(self, name, email, age):
    self.name = name # self is like this in JS
    self.email = email
    self.age = age  
    
  # add a method
  # we need to use "self" to access the properties of the class
  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age += 1

# End of class


# init user object
brad = User('Brad', 'email@email.com', 30)

# call has_birthday method
brad.has_birthday()

# call greeting method and print result
print(brad.greeting())




print(type(brad))
print(brad.name)
print(brad.email)
print(brad.age)



# Extend class
# in JS class Customer extends User {....}
class Customer(User): # Customer class inherits from User class
  # constructor
  def __init__(self, name, email, age):
    self.name = name # self is like this in JS
    self.email = email
    self.age = age
    self.balance = 0

  # add a method, set_balance  
  def set_balance(self, balance):
    self.balance = balance
    
  # override greeting method from User class
  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
    
# init customer object
janet = Customer('Janet Johnson', 'janet@email.com' , 25)

janet.set_balance(500)

print(janet.greeting())

