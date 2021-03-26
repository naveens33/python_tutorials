class Student:
    #properties / data members
    name = ''
    rollno=0
    schoolname = ''

    #behaviour / member methods
    def display_details(self):
        print(self.name, self.rollno)

    def display_completedetails(self):
        print(self.name,self.rollno,Student.schoolname)

    @staticmethod
    def display_schoolname():
        print(Student.schoolname)

Student.schoolname ="Don Bosco"
Student.display_schoolname()
s1 = Student()
s2 = Student()
s1.name="Prem"
s1.rollno=33
s1.display_details()
s2.name="Somi"
s2.rollno=56
s2.display_details()
s1.display_completedetails()
s2.display_completedetails()