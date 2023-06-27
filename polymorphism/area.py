class CalculateArea:
    '''
    But Python does not support function overloading. An error gets thrown if we implement the function overloading
    code the way we do in other languages. The reason is as Python does not have a data type for method parameters.
    '''
    def area(self,x,y=None):
        if y ==None:
            print(3.14*x*x)
        else:
            print(x*y)


if __name__=='__main__':
    c=CalculateArea()
    c.area(5)
    c.area(5,8)
