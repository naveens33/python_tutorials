class cal_area:
    def area(self,x,y=None):
        if y is None:
            print(3.14*x*x)
        else:
            print(x*y)

c = cal_area()
c.area(5)
r = cal_area()
r.area(5,6)

