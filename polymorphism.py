#Overriding
class parent:
    def display(self):
        print('This is parent')

class child(parent):
    def display(self):
        #super().display()
        print('This is child')

if __name__=='__main__':
    c_obj=child()
    c_obj.display()

    #p_obj=parent()
    #p_obj.display()

#Overloading
#python does not supports method overloading
class area:
    def calculate(self,radius):
        answer=radius*radius
        print("Area of the circle: "+str(answer))
    def calculate(self,length,width):
        answer=length*width
        print("Area of the rectangle: "+answer)

if __name__=='__main__':
    obj=area()
    obj.calculate(4)
    obj.calculate(4,7)