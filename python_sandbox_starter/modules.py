# A module is basically a file containing a set of functions to include 
# in your application. There are core python modules, modules you can 
# install using the pip package manager (including Django) 
# as well as custom modules


# core modules
import datetime # imports core module
from datetime import date # import specific class
# import time
from time import time

#pip modules
from camelcase import CamelCase

today = datetime.date.today()
print(today)

today2 = date.today()
print(today2)

timestamp = time()
print(timestamp) # 1615790000.0

# timestamp2 = time()
# print(timestamp2) # 1615790000.0

# convert timestamp to date and time
print(datetime.datetime.fromtimestamp(timestamp)) # 2021-03-15 12:20:00


c = CamelCase()
print(c.hump('hello there world')) # HelloThereWorld  

# import custom module
from validator import validate_email


email = 'test#testemailcom'
if validate_email(email):
  print('Email is valid')
else:
  print('Email is bad')
  

