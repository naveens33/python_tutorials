class Student:
    rollno=0
    name=""

    def displayDetails(self):
        print(self.rollno,self.name)


if __name__=='__main__':
    s1=Student()
    s2=Student()
    s1.rollno=1
    s1.name="Anish"
    s2.rollno=2
    s2.name="Anto"
    s1.displayDetails()