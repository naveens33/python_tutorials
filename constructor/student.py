class Student:
    name = ''
    rollno = 0

    def __init__(self,n,r):
        self.name = n
        self.rollno = r

    def display_details(self):
        print(self.name, self.rollno)

s1 = Student("Prem",33)
s2 = Student("Somi",56)
s1.display_details()
s2.display_details()
