#Inheritance
class Student:
    firstname=""
    lastname=""
    schoolname="Don Bosco"
    def name(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

class CompleteDetails(Student):
    def details(self):
        return self.schoolname+"- "\
               +self.firstname+", "+self.lastname

s1=CompleteDetails()
s1.name('Roman','Reigns')
print(s1.details())

#Multiple Inheritance
class Student:
    firstname=""
    lastname=""
    schoolname="Don Bosco"
    def name(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

class BusFee():
    paid=""
    def setdetails(self,status):
        self.paid=status

class CompleteDetails(Student,BusFee):
    def details(self):
        return self.schoolname+"- "+self.firstname+", "+self.lastname+" Bus Fee Status: "+self.paid

s1=CompleteDetails()
s1.name('Roman','Reigns')
s1.setdetails("Yes")
print(s1.details())

#Private Variable
class Student:
    firstname=""
    lastname=""
    schoolname="Don Bosco"
    def name(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

class Address():
    _address=""
    def setaddress(self,address):
        self._address=address

class CompleteDetails(Student,Address):
    def details(self):
        return self.schoolname+"- "+self.firstname+", "+self.lastname+" Address: "+self._address
if __name__=='__main__':
    s1=CompleteDetails()
    s1.name('Roman','Reigns')
    s1.setaddress("Bangalore")
    print(s1.details())
    s1._address="hello"
    print(s1._address)