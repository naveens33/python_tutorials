'''List a mutable In Python, Assignment statements do not copy objects, they create bindings between a target and an
object. When we use = operator user thinks that this creates a new object; well, it doesn’t. It only creates a new
variable that shares the reference of the original object '''
li1 = [12, 22, 32, 42]
li2 = []
li2 = li1
li2.append(52)
print(li1)
print(id(li1))
print(li2)
print(id(li2))
# li2 is actually reference to object(li1)

print("********** Shallow copy ************")

import copy

li1 = [12, 22, [32, 42]]
li2 = copy.copy(li1)
li2[0] = 2
print(li1)
print(li2)

# changing the element in the object(li2) doesnt change the original object(li1)

print("********** Shallow copy change the nested list ************")

li1 = [12, 22, [32, 42]]
li2 = copy.copy(li1)
li2[2][1] = 2
print(li1)
print(li2)

# Shallow copy create a copy of the object but references each element of the object, here li1[2] is an list object not an element
#if element -> copy
#if object -> reference

print("********** Deep copy ************")

li1 = [12, 22, [[32,34], 42]]
li2 = copy.deepcopy(li1)
li2[2][1] = 2
li2[2][0][1] = 2
print(li1)
print(li2)

# Deep copy creates a copy of the object and the elements of the object
