#define class and object
class Class_Name:
  var = 33

obj1 = Class_Name()
print(obj1.var)

#Self Explain
class Displaystr(object):
    str = "hello"
    def display(self):
        #str = str + "hi"
        str=self.str+"hi"
        print(str)

x=Displaystr()
print(x.str)
x.display()

#Built-in __init__() function
class School:
  name=""
  fname=""
  def __init__(self, n, fn):
    self.name = n
    self.fname = fn

p1 = School("Prem", "kumar")

print(p1.name)
print(p1.fname)
