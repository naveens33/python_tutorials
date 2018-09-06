list = [ 'anish,', 'somesh' , 'sankar', 3]
print(list)
#Access Items
print(list[2])
#Change Item Value
list[2]="suresh"
print(list)

#functions
#length
print(len(list))
#Add Item at last
list.append("haresh")
#Add Item in specified location
list.insert(3, 4)
#Remove specific item
list.remove("haresh")
#pop method - removes the specified index, (or the last item if index is not specified)
list.pop()
print(list)
#clear method
list.clear()
print(list)