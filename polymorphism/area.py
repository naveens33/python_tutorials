class CalculateArea:
    def area(self,x,y=None):
        if y ==None:
            print(x*x)
        else:
            print(x*y)


if __name__=='__main__':
    c=CalculateArea()
    c.area(5)
    c.area(5,8)