"""
list store sequence of values
List items are in square brackets, separated with "," [ 1, 34, 54 ]
"""

#Empty list
empty_list = []
print(empty_list)

li1 = [1, 34, 54, 65, 76]

# Indexing
print(li1[3])

# Slicing
print(li1[2:4])
print(li1[-4:-2])

# Reversing
print(li1[::-1])

# Operators
# Arithmetic operators
li2 = [99, 78, 34]
print(li1 + li2)

print(li1 * 3)

# Logical operator
print(54 in li1)
print(76 not in li1)

# list can have any type
li3 = [12, 34.56, True, "Hello", [1, 2, 3]]
print(li3[4][2])

print(li1)
# for loop
for i in li1:
    print(i)

# randomize the items of a list
from random import shuffle

x = [99, 55, 78, 63, 45, 1, 12, 15]
shuffle(x)
print(x)
