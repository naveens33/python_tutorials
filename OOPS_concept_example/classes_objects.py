#define class and object
class Class_Name:
  var = 33

obj1 = Class_Name()
print(obj1.var)

#Self Explain
class Displaystr:
    str = "hello"
    def display(self):
        #str = str + "hi"
        str=self.str+"hi"
        print(str)

x=Displaystr()
print(x.str)
x.display()

class student:
    rollno=0
    name=""
    def setvalue(self,x,y):
        self.rollno=x
        self.name=y

    def print(self):
        print(self.rollno)
        print(self.name)

if __name__=="__main__":
    s1=student()
    s1.setvalue(45,"sankar")
    s1.print()
