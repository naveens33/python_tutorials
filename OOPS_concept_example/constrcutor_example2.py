class Student:
    rollno=0
    name=""

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

    def displayDetails(self):
        print(self.rollno,self.name)

    def __del__(self):
        print("this is destructor")

if __name__=='__main__':
    s1=Student(1,"Anish")
    s2=Student(2,"Anto")
    s1.displayDetails()
    del(s1)
    s2.displayDetails()
