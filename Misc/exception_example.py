#This statement will raise an error, because fname is not defined:
try:
  print(fname)
except:
  print("An exception occurred")

#Many Exceptions
try:
  print(fname)
except NameError:
  print("Variable fname is not defined/declared")
except:
  print("Different error")

#Else

try:
  print("Hello, World")
except:
  print("Error")
else:
  print("Nothing went wrong")

#Finally
try:
  print(fname)
except:
  print("Variable fname is not defined/declared")
finally:
  print("The 'try except' is finished")