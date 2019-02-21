# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.

a = [1,2,3,4] # Point a at a new list
b = a         # b points at what a points to
b is a        # True, a and b refer to same object
b == a        # True, a and b objects are equal
b = [1,2,3,4] # Point b at a new list
b is a        # False, a and b do NOT refer to the same object
b == a        # True, a and b objects are still equal

"{} can be {}".format("Strings", "Interpolated") # 'Strings can be interpolated'

"{0} can be quick, {0} can be fast, and he is {1}".format("Nurul", "Fast")

# Input data from console
input_string_var = input("Enter some data: ") # Returns a string

# Lists store sequences
List = [4,5,6]

List.append(7) # Add 7 to end of list so [4,5,6,7]

List.pop() # Removes 7

List[1:3] # Provides [5,6] - Sliced Index

# List[Start:End:Step]
List[::2] # Provides [4,6] - Every second entry

List [::-1] # Reversed List

del List[2] # Removes 6

List2 = List[:] # Copy list into list2

List.remove(5) # Removes first occurence of 5

List.insert(1,5) # Insert 5 at index 1

List.index(4) # Provides 0 as it gives the index of the first item found

# You can add lists

List.extend(List2) # Concatenate lists

# Tuples are immutable lists
tup = (1,2,3)

a,b,c = (1,2,3) # a=1 etc

a, *b, c = (1,2,3,4) # b=[2,3]

# Dictionaries store mappings to values
dict = {"one": 1, "two": 2, "three": 3}

dict.get("one")

list(dict.keys())
list(dict.values())
dict.update({"four":4})
dict.update["four"] = 4

# Sets store .. sets with immutable elements
set = {1,1,2,2,3,4} # Set is now {1,2,3,4}
set2 = {(1,2),3}

def varargs(*args):
    return args

def keyword_args(**kwargs):
    return kwargs





