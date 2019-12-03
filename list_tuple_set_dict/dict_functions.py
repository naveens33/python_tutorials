d={"Name":"John","Class":2,"Rank":1,"FeeStatus":["paid","paid","paid"]}

#get
print(d.get("FeeStatus"))
print(d["FeeStatus"])

#dict item related fucntions
print(d.keys())
print(d.values())
print(d.items())

#popitem pop del
d.popitem()
print(d)

d.pop("Class")
print(d)

del(d["Name"])
print(d)