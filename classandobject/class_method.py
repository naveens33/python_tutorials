class Student:
    name=""
    rollno=0
    city=""

    @classmethod
    def display(cls):
        print(Student.name,Student.rollno)
        print(cls.city)

Student.name="PRem"
Student.rollno=34
Student.display()