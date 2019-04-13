class CalcArea:

    def area(self,x,y=None):
        if y==None:
            ans=x*x
            print("Area of Circle is: ",ans)
        else:
            ans=x*y
            print("Area of Rectangle is: ", ans)

if __name__=='__main__':
    obj=CalcArea()
    obj.area(5)
    obj.area(4,6)

