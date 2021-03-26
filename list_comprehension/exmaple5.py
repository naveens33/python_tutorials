names = ['Evangeline Rennie','Shanae Coulson','Cassius Mcbride','Sofia Thomas']
li = [(name, len(name)) for name in names]
print(li)

li = [{name:len(name)} for name in names]
print(li)