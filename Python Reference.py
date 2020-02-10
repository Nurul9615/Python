# (is vs. ==) is checks if two variables refer to the same object, but == checks if the objects pointed to have the same values.

a = [1,2,3,4] # Point a at a new list
b = a         # b points at what a points to
b is a        # True, a and b refer to same object
b == a        # True, a and b objects are equal
b = [1,2,3,4] # Point b at a new list
b is a        # False, a and b do NOT refer to the same object
b == a        # True, a and b objects are still equal

"{} can be {}".format("Strings", "Interpolated") # 'Strings can be interpolated'

"{0} can be quick, {0} can be fast, and he is {1}".format("Nurul", "Fast")

"This is a String"[0] # -> T

name = "Ray"
f"Her name is {name}"
f"{name} is {len(name)} characters long"

"print this" if 3 > 2 else 2 # if used as an expression

# Input data from console
input_string_var = input("Enter some data: ") # Returns a string

# Lists store sequences
List = [4,5,6]

List.append(7) # Add 7 to end of list so [4,5,6,7]

List.pop() # Removes last element 7

List[1:3] # Provides [5,6] - Sliced Index - End index is not included

# List[Start:End:Step]
List[::2] # Provides [4,6] - Every second entry

List [::-1] # Reversed List

del List[2] # Removes 6

List2 = List[:] # Copy list into list2

List.remove(5) # Removes first occurence of 5

List.insert(1,5) # Insert 5 at index 1

List.index(4) # Provides 0 as it gives the index of the first item found

List1 + List 2 # Add lists

List.extend(List2) # Concatenate lists

1 in List # -> True

# Tuples are immutable lists
# Tuples of length one need a comma after first element 
tup = (1,2,3)

a,b,c = (1,2,3) # Unpacking tuples - a=1 etc

a, *b, c = (1,2,3,4) # Extended unpacking - b=[2,3]

d, e, f = 4, 5, 6 # Also a tuple

# Dictionaries store mappings to values
# Keys must be immutable types like ints, floats, strings, tuples
dict = {"one": 1, "two": 2, "three": 3}
dict["one"] # -> 1

dict.get("one")

list(dict.keys()) # ["one", "two", "three"]

list(dict.values()) # [1,2,3]

"one" in dict # -> True - Looks for keys

dict.update({"four":4})

dict.update["four"] = 4

del dict("one")

# Sets store sets with immutable elements
set = {1,1,2,2,3,4} # Set is now {1,2,3,4}
set2 = {(1,2),3}

set2.add(5)

set & set2 # Set intersection
set | set2 # Set union

# Conditional loops

if number > 10:
    print("alright")
elif number < 10:
    print("ok")
else:
    print("fine")

for number in ["one", "two", "three"]:
    print("{} is a number".format(number))

for i in range(4,8,2):
    print(i)
    # 4, 6 (Ignores 5 and 7 as step is 2)

animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)
    '''
    0 dog
    1 cat
    2 mouse
    '''

x = 0
while x < 4
    print(x)
    x += 1

try:
    raise IndexError("This is index error")
except IndexError as e:
    pass
except (TypeError, NameError):
    pass
else:
    print("good")
finally:
    print("nice")

# Writing to files

with open("file.txt") as f:
    for line in f:
        print(line)

with open("file.txt", "w+") as file:
    file.write(str(dictionary))

with open("file.txt", "r+") as file:
    contents = file.read()
print(contents)

# Functions

def add(x,y):
    print("x is {} and y is {}".format(x,y))
    return x + y

def varargs(*args): # Variable number of positional arguments
    return args

def keyword_args(**kwargs): # Variable number of keyword arguments
    return kwargs

keyword_args(big="foot", loch="ness")

def create_Adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_Adder(10)
add_10(3) # -> 13