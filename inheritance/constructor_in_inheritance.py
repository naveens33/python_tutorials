class parent:
    def __init__(self):
        print("Parent_Cons")

    def display1(self):
        print("Hello")

class child(parent):
    def __init__(self):
        #parent.__init__(self)
        #self.display1()
        super().__init__()
        print("Child_Cons")

    def display2(self):
        print("World")

if __name__=='__main__':
    c=child()
    c.display2()