# Indexing
# Slicing -> Substring
# Reversing
# Contains
# Concatenating
# Repeat
# working with loops
'''
    Indexing and Slicing
'''
var1 = "Python"
var2 = "Tutorial"

#+ve indexing
print ("var1[0]:",var1[2])
#-ve indexing
print ("var1[0]:",var1[-3])

#+ve slicing
print ("var2[1:5]:",var2[1:5])

#-ve slicing
print ("var2[1:5]:",var2[-5:-2])

#Reverse a complete string
print("Reverse a complete string",var2[::-1])

#Reverse a substring
print("Reverse a substring", var2[5:2:-1])
'''
    Operators with string
'''
#Logical operator in and not
print("in")
print("y" in var1)

print("not in")
print("u" not in var1)

#Arithmetic operator +(concadinate) and *(repeat)
print(var1+var2)
print(var1 * 10)

#working with loop
#By Indexing
name="Don Bosco"
for i in range(0,len(name)):
    print(name[i])

#By Iterable
name="Don Bosco"
for c in name:
    print(c)

