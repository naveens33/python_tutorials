class FindTotal:
    def total(self,m1,m2,m3):
        return m1+m2+m3

class FindAverage:
    def average(self,t,noofsub):
        return t/noofsub


class Marklist(FindTotal,FindAverage):
    mark1=0
    mark2=0
    mark3=0

    def __init__(self,m1,m2,m3):
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3

    def printMarkList(self):
        t=self.total(self.mark1,self.mark2,self.mark3)
        a=self.average(t,3)
        print("Total: ",t)
        print("Average: ", a)

if __name__=='__main__':
    s1=Marklist(34,65,87)
    s1.printMarkList()