import datetime

obj = datetime.datetime.now()
print("Date Time: "+str(obj))
print("Year: "+str(obj.year))
print("Date: "+str(obj.strftime("%d")))
print("Day: "+str(obj.strftime("%A")))
print("Month: "+str(obj.strftime("%B")))


