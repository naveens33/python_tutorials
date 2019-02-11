# Creating tuples
tupl1 = 'AC', 'TV'
print(tupl1)

tupl2 = ('remote', 'tv')
print(tupl2)


# Nested tuples
tupl3=(tupl1,tupl2)
print(tupl3)

tupl4=('Hi',)*3
print(tupl4)

#Slicing
tupl5 = (91,94,96,99)
print(tupl5[1:])
print(tupl5[:-1])
print(tupl5[2:4])

#Deleting
del(tupl5)
#print(tupl5)

#length
tupl6 = (91,94,96,99)
print(len(tupl6))

#max() , min()
tupl7=(97,94,96,99)
tupl8=(91,94,96,9)
print(min(tupl7))
print(max(tupl8))