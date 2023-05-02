li1 = [34, "Hello", True, 89.56, [54,87, 45]]

li2 = li1

print("li1",li1)
print("li2",li2)

print("Change the value in li1")

li1[2] = "Somi"

print("li1",li1)
print("li2",li2)


print("After Shallow copy")

li3 = li1.copy()
li1[1] = "World"

print("li1",li1)
print("li2",li2)
print("li3",li3)

li1[4][0] = 100
print("********************************")
print("li1",li1)
print("li2",li2)
print("li3",li3)

print("After deep copy")
from copy import deepcopy
li4 = deepcopy(li1)

li1[4][1] = 500
print("li1",li1)
print("li2",li2)
print("li3",li3)
print("li4",li4)