#dictionary
dict1 = {"Name": 'Naveen', 'Class': "Tenth", 'Section': 'A'}
print(dict1['Name'])
dict1['Name']="prem"
print(dict1)

#Updating Dictionary
dict2 = {'Name': 'Naveen', 'Class': "Tenth", 'Section': 'A'}
dict2['Class'] = "Eigth";
dict2['Rank'] = 2;
print ("dict['Class']: ", dict2['Class'])
print ("dict['Rank']: ", dict2['Rank'])
print(dict2)

#Delete Dictionary/Elements
dict3 = {'Name': 'Naveen', 'Class': "Tenth", 'Section': 'A'}
del dict3['Name'];
print(dict3)
dict3.clear();

#del dict3 ;

#print ("dict3['Name']: ", dict3['Name'])
#print ("dict3['Section']: ", dict3['Section'])

#for loop
dict4 = {'Name': 'Naveen', 'Class': "Tenth", 'Section': 'A'}
for x in dict4:
  print(dict4[x])

#len
dict5 = {'Name': 'Naveen', 'Class': "Tenth", 'Section': 'A'}
print(len(dict5))

#str
dict6 = {'Name': 'Naveen', 'Class': "Tenth", 'Section': 'A'}
print(str(dict6))

#type
dict7 = {'Name': 'Naveen', 'Class': "Tenth", 'Section': 'A', 'Rank':4}
print(type(dict7['Name']))
print(type(dict7['Rank']))
