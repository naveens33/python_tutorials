s1={12,34.56,True,"Hello"}

#add
s1.add("World")
print(s1)

#remove and clear
s1.remove(True)
print(s1)

s1.pop()
print(s1)

s1.clear()
print(s1)

#set based functions
s1={12,34.56,True,"Hello"}

s2={12,34.56,False,"World"}

print(s1.difference(s2))
print(s2.difference(s1))
print(s1.union(s2))
print(s1.intersection(s2))

