d={"Name":"John","Class":2,"Rank":1,"FeeStatus":["paid","paid","paid"]}

#key value pair relationship seperated by commas
#As like set, we cannot have list or tuple on key but values can have list or tuple
print(d)

#indexing and slicing, since, with the subscript we can get the value with the help of key
#print(d[1])
print(d["Name"])

#add new key in the dict
d["City"]="Bangalore"
print(d)

#update
d["Class"]=4
print(d)

#for loop
for k in d.keys():
    print(d.get(k))

for v in d.values():
    print(v)