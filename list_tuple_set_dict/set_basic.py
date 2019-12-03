s={12,34.56,True,"Hello"}

#set will not preserve the element order. so, indexing and slicing is not possible
print(s)

s.add(True)
#Cannot have a duplicate element
print(s)

#Cannot have list, tuple and dict
s.add([1,2,4])
print(s)
