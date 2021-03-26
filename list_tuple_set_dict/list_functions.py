"""
Built-in methods to help manipulating a list
"""

li1=[12,34.56,True,"Hello",[1,2,3]]

#index and count
print(li1.count(34.56))
print(li1.index([1,2,3]))

#insert,append and extend the list
li1.append("World")
print(li1)
li1.insert(2,790)
print(li1)
li2=["bob","alice"]
li1.extend(li2)
print(li1)

# pop remove clear del
li1.pop()
print(li1)
li1.pop(3)
print(li1)
li1.remove("World")
print(li1)
del(li1[2])
print(li1)
#del(li1)
#print(li1)
#li1.clear()
#print(li1)

#Reverse
li1.reverse()
print(li1)

#Sort -> You cannot sort list which having another nested list
li1.sort()
print(li1)

#in list we can able to have tuple, set and dict
li1.append({1,2,3,4})
print(li1[5])