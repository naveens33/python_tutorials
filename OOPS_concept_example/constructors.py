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

#Deleting Objects/Destructor
class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

    def __del__(self):
       print("this is destructor")

c1 = ComplexNumber(2,3)
c1.getData()
del(c1)
#c1.getData()

