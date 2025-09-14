# %%
my_list = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
]

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    # print(char, ord(char))
    sum_of_chars += ord(char)

  return sum_of_chars % 10

def add(name):
   index = hash_function(name)
   my_list[index].append(name)

def contains(name):
  index = hash_function(name)
  return name in my_list[index]
# %%
if __name__ == "__main__":
    print("'Bob' has hash code:", hash_function('Bob'))
    add('Bob')
    add('Pete')
    add('Jones')
    add('Lisa')
    add('Siri')
    add('Stuart')
    print(my_list)
    print("Contains 'Bob':", contains('Bob'))
    print("Contains 'Lisa':", contains('Lisa'))
    print("Contains 'Stuart':", contains('Stuart'))
    print("Contains 'Alice':", contains('Alice'))
# %%
