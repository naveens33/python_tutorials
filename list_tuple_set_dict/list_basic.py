li1=[1,34,54,65,76]

#Indexing
print(li1[3])

#Slicing
print(li1[2:4])
print(li1[-4:-2])

#Reversing
print(li1[::-1])

#Operators
#Arithmetic operators
li2=[99,78,34]
print(li1+li2)

print(li1*3)

#Logical operator
print(54 in li1)
print(76 not in li1)

#list can have any type
li3=[12,34.56,True,"Hello",[1,2,3]]
print(li3[4][2])

print(li1)
#for loop
for i in li1:
    print(i)