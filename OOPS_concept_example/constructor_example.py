class MarkList:
    mark1=0
    mark2=0
    mark3=0

    def __init__(self,m1,m2,m3):
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3

    def getTotal(self):
        total=self.mark1+self.mark2+self.mark3
        return(total)

    def getAverage(self,t,noofsub):
        avg=t/noofsub
        return avg

if __name__=='__main__':
    s1=MarkList(100,89,98)
    c=s1.getTotal()
    d=s1.getAverage(c,3)
    print(c)
    print(d)