# %%
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# %%
print(thislist[:4])
# %%
print(thislist[4:])

# %%
print(thislist[-4:-1])
# %%
thislist[1] = "blackcurrant"
print(thislist)
# %%
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# %%
thislist2 = ["apple", "banana", "cherry"]
# %%
thislist2[1:3] = ["blackcurrant"]
print(thislist2)
# %%
thislist2.insert(2, "windows")
# thislist2.append("macintosh")
print(thislist2)
# %%
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# %%
fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
print(newlist)
# %%
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# %%


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)
# %%
print(abs(-100))

# %%
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# %%
# %%
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
# %%
coordinates = (10.5, 20.3)
# coordinates[0] = 15   ❌ TypeError (not allowed)
print(coordinates)  # (10.5, 20.3)

# Tuples can be used as dict keys
locations = {coordinates: "My Location"}
print(locations)  # {(10.5, 20.3): 'My Location'}

# %%
locations = {1: "My Location"}
print(locations)  # {(10.5, 20.3): 'My Location'}
# %%
thistuple = ("apple",)
print(thistuple)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(thistuple)
print(type(thistuple))

# %%
# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
# %%
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
# %%
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
# %%
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(*green, tropic, red) = fruits

print(green)
print(tropic)
print(red)
# %%
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
# %%
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
# %%
thisset = {"apple", "banana", "cherry"}
print(thisset)
# %%
thisset = {"apple", "banana", "cherry", "Apple"}

print(thisset)
# %%
thisset = {"apple", "banana", "cherry", True, 1, 2}

# %%
print(thisset)
# %%
set1 = {"apple", "banana", "cherry"}
print(set1)
set2 = {1, 5, 7, 9, 3}
print(set2)
set3 = {True, False, False}
print(set3)

# %%
set1 = {"abc", 34, True, 40, "male"}
print(set1)
# %%
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
# %%
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
# %%
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange", "cherry"]

thisset.update(mylist)

print(thisset)
# %%
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
thisset.discard("cherry")

# thisset.remove("papaya") # KeyError: 'papaya'
thisset.discard("papaya")

print(thisset)

# %%
thisset = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}

x = thisset.pop()

print(x)

print(thisset)
# %%
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set1)
print(set3)
# %%
# %%
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
# %%
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
# %%
set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "d", "a"}
print(set1 | set2)

set1.update(set2)
print(set1)
# %%
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
set3 = set1 & set2

print(set3)
# %%
# %%
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = {"flowers", "animals", "bottles"}

set4 = set1 & set2 & set3
print(set4)
# %%
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
# %%
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)
# %%
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
# %%
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
# %%
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
# %%
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
# %%
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
# %%
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
# %%
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
    "level1": {"level2": {
        "level3": "value"}
    },
    5: "hello"
}
# print(len(thisdict))
# print(thisdict)
print(thisdict.keys())
print(thisdict.values())
x = thisdict.items()
print(x)
# %%
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change


# %%
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
    "level1": {"level2": {
        "level3": "value"}
    },
    5: "hello"
}
for x in thisdict:
    print(thisdict[x])
# %%
for x in thisdict.values():
    print(x)  # %%

# %%
for x in thisdict:
    print(x)
# %%
for x, y in thisdict.items():
    print(f'{x}: {y}')
# %%
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])
# %%
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")


# %%
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif b < a:
  print("a is greater than b")
# %%
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
# %%
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# %%
def changecase(func):
    print("Inside changecase")
    def wrapper():
        print("Inside wrapper")
        return  func().upper()
    return wrapper

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())
# %%
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
# %%
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
# %%
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))
# %%
a = [1, 2, 3]
b = a
del(a)
print(b)   # still works, because 'b' references the list

# %%
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
# %%
mystr = "banana"
myit = iter(mystr)
# %%
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# %%
for _ in range(len(mystr)):
  print(next(myit), end=' ')
# %%
mystr = "banana"

for x in mystr:
  print(x)
# %%
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# %%
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in range(22):
  print(next(myiter))

print(next(myiter))  # StopIteration
# %%
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
# %%
import platform

x = platform.system()
print(x)
print(dir(platform))
# %%
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
print(x.strftime("%d-%m-%Y"))
# %%

import math
print(len(dir(math)))
print('\n'.join(x for x in iter(dir(math))))

# %%
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
z = dict(name="muthu", age=31, city="Nebraska")
z1 = {1:"unknown", "name":"muthu", "age":"31", "city":"Nebraska"}
print(z1)
# parse x:
y = json.loads(x)
z2 = json.loads(z1)
print(z2)
# %%
# the result is a Python dictionary:
print(z)
print(x)
print(y)
print(y["age"])
print(type(y))
print(json.dumps(z))
# %%
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
# %%
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x))
# print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, sort_keys=True))
# print(json.dumps(x, indent=4, separators=(". ", " = ")))

# %%

import json
z1 = {1:"unknown", "name":"muthu", "age":"31", "city":"Nebraska"}
print(z1)
print(json.dumps(z1))
#%%
z2 = json.loads(json.dumps(z1))
print(z2)
# %%
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
y = re.findall("^The.*SKpain$", txt)
print(x)
print(x.start())
print(x.end())
print(x.group())
print(x.string)
print(x.span())
print(y)
# print(y.group())
# print(x.match)
# %%
import re

txt = "The rain in Spain"
x = re.search("^.*S.*$", txt)

print("The first white-space character is located in position:", x.start())
# %%
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
# %%
import re

txt = "The rain in Spain"
x = re.split(r"\s", txt, 2)
print(x)
# %%
import re

txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt, 2)
print(x)
# %%
import re

txt = "The rain in Spain"
x = re.search(r"^The.*Spain$", txt)
# x = re.search(r"\bS\w+", txt)
print(x.group())
print(x.string)


# %%
import re
txt = 'The rain in Spain'
x = re.findall('[a-sA-S]', txt)
print(x)
# %%
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
# %%
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
# %%
txt = f"The price is 49 dollars"
print(txt)
# %%
price = 59
txt = f"The price is {price} dollars"
print(txt)
# %%
price = 59.0
txt = f"The price is {price:.2f} dollars"
print(txt)
# %%
txt = f"The price is {95:.2f} dollars"
print(txt)
# %%
txt = f"The price is {20 * 59} dollars"
print(txt)
# %%
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)
# %%
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)
# %%
txt = f"We have {49:<8} chickens."
print(txt)
# %%
txt = f"We have {49:>8} chickens."
print(txt)
# %%
txt = f"We have {49:^7} chickens."
print(txt)
# %%
txt = f"We have {-49:=} chickens."
print(txt)
# %%
txt = f"We have {49:+} chickens."
print(txt)
# %%
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
print(f"I want {quantity} pieces of item number {itemno} for {price:.2f} dollars.")
# %%
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
# %%
# %%
age = 36
name = "John"
txt = "His name is {}. {} is {} years old."
print(txt.format(name, name, age))
# %%
print("Enter your name:")
name = input()
print(f"Hello {name}")
# %%
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")
# %%
my_array = [7, 12, 9, 4, 11, 8]
print(min(my_array))
# %%

str = "hello welcome to my world"
str1 = "hello1234"
str2 = "Hello"
str3 = " "
print(str1.isalnum())
print(str2.isalpha())
print(str1.isdecimal())
print(str1.isnumeric())
print(str1.isdigit())
print(str.islower())
print(str.isprintable())
print(str3.isspace())
# %%
# Creating frozenset
fs = frozenset([1, 2, 3, 2, 1])
print(fs)   # frozenset({1, 2, 3})

# Immutable → cannot do fs.add() or fs.remove()
# fs.add(4)  # ❌ AttributeError

# But you can still do set operations
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print(a | b)  # frozenset({1, 2, 3, 4, 5})
print(a & b)  # frozenset({3})

# %%

# def len(name):
#    print("Hello", name)

len("muthu")

my_list = [1, 2, 3]
print(len(my_list))

# %%
str = "Hello"
st1 = 'Hello'
print(str is st1)
# %%
str = "Hello"[0]
print(str)
# %%
str = " Hello "
print(str.strip())
print(str.trim())

# %%
str = "Hello"
print(str.replace("H", "J"))
# %%
my_list = [10, 20, 30, 20, 40, 20]
print(list(enumerate(my_list)))
# indexes = [i for i, x in enumerate(my_list) if x == 20]
# print(indexes)  # [1, 3, 5]
# %%
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.add('muthu')

print(thisset)
# %%