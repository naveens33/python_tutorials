class Marksheet:
    mark1=0
    mark2=0
    mark3=0
    def __init__(self,x,y,z):
        self.mark1=x
        self.mark2=y
        self.mark3=z

    def total(self):
        t=self.mark1+self.mark2+self.mark3
        print(t)

if __name__=="__main__":
    student1=Marksheet(90,67,84)
    #student2 = Marksheet()
    student1.total()

    #student2.total()