import weakref
class student:
    rollno=0
    feestatus=False

    def print_fee_status(self):
        print(self.rollno,self.feestatus)

if __name__=='__main__':
    s1=student()
    s2=student()
    s1.rollno=675
    s1.feestatus=True
    s2.rollno=676
    s2.feestatus=False
    s1.print_fee_status()
    s2.print_fee_status()
    s3=weakref.ref(s1)
    s1=None
    print(s3, s1)