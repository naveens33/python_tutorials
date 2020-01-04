class GrandParent:
    def display1(self):
        print("GP")

class Parent(GrandParent):
    def display2(self):
        print("P")

class Child(Parent):
    def display3(self):
        print("C")

if __name__=='__main__':
    c= Child()
    c.display1()