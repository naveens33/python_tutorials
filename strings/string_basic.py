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
print ("var2[1:5]:",var2[-2:-5])

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
