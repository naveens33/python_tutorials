# monkey patch refers to dynamic (or run-time) modifications of a class or module

class calc:
    def equal(self,x,y):
        pass


def add(self,x,y):
    print(x+y)

def sub(self,x,y):
    print(x-y)

option = input("Enter the option to perform add/sub ")
if option == "add":
    calc.equal = add
else:
    calc.equal = sub
obj = calc()
obj.equal(5,6)