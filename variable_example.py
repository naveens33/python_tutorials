print("Redeclare a Variables ")
# Declare a variable and initialize it
a = 0
print (a)
# re-declaring the variable works
a="hello"
print(a)

print("Concatenate Variables-  TypeError: can only concatenate str (not 'int') to str")

#a="naveens"
#b = 33
#print (a+b)

print("Concatenate Variables-  No Error")

a="naveens"
b = 33
print (a+str(b))

print ("Local & Global Variables")
# Declare a variable and initialize it
var = 56
print (var)
# Global vs. local variables in functions
def Function():
# global f
    var = 'Python tutorial'
    print (var)
Function()
print (var)

print("Delete a variable")
a = 27;
print(a)
del a
print(a)