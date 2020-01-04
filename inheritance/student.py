class MarkCalculator:
    def total(self,m1,m2,m3,m4,m5):
        return(m1+m2+m3+m4+m5)

    def avg(self,t,s):
        return (t/s)


class Student(MarkCalculator):
    rollno=0
    m1,m2,m3,m4,m5=0,0,0,0,0

    def __init__(self,m1,m2,m3,m4,m5):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5

    def displayRankCard(self):
        t=self.total(self.m1,self.m2,self.m3,self.m4,self.m5)
        a=self.avg(t,5)
        print(t, a)


if __name__=='__main__':
    s1=Student(23,54,76,98,98)
    s1.displayRankCard()