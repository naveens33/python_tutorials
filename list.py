# empty list
my_list = []
#print(my_list[0])

# list of integers
my_list = [1, 2, 3]
print(my_list[1])

# list with mixed datatypes
my_list = [1, "Hi", 56.48]
print(my_list[2])

# nested list
my_list = ["hello", [23, 3, 67], ['c']]
print(my_list[1][2])

#Negative indexing
my_list = ['t','u','t','o','r','i','a','l']

# Output: a
print(my_list[-2])

# Output: r
print(my_list[-4])

#slice lists in Python
my_list = ['l','a','g','u','a','g','u','e']
# elements 3rd to 5th
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])

#append() method & extend() method
odd = [1, 3, 5]

odd.append(7)

# Output: [1, 3, 5, 7]
print(odd)

odd.extend([9, 11, 13])

# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)


#+ operator & * operator
odd = [1, 3, 5]

# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])

#Output: ["re", "re", "re"]
my_list=["re"]*3
print(my_list)

#insert()
odd = [1, 9]
odd.insert(1,3)

# Output: [1, 3, 9]
print(odd)

odd[2:2] = [5, 7]

# Output: [1, 3, 5, 7, 9]
print(odd)

#del
my_list = ['p','y','t','h','o','n']

# delete one item
del my_list[2]

# Output: ['p', 'y', 'h', 'o', 'n']
print(my_list)

# delete multiple items
del my_list[1:5]

# Output: ['p']
print(my_list)

# delete entire list
del my_list

# Error: List not defined
#print(my_list)

#remove() pop() clear()
rpc_list = ['b','a','n','g','a','l']
rpc_list.remove('b')

# Output: ['a', 'n', 'g', 'a', 'l']
print(rpc_list)

# Output: 'n'
print(rpc_list.pop(1))

# Output: ['a', 'g', 'a', 'l']
print(rpc_list)

# Output: 'l'
print(rpc_list.pop())

# Output: ['a', 'g', 'a']
print(rpc_list)

rpc_list.clear()

# Output: []
print(rpc_list)