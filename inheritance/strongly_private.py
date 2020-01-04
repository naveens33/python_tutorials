class parent:
    def __display1(self):
        print("Hello")

    def display3(self):
        self.__display1()

class child(parent):
    def display2(self):
        print("World")

if __name__=='__main__':
    c=child()
    c.display3()