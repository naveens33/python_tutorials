class parent:
    def __init__(self,x):
        print("This is Parent Constructor", x)

    def display(self):
        print("Hello")

class child(parent):
    def __init__(self,x):
        print("This is child Constructor",x)
    def display(self):
        print("World")

if __name__=='__main__':
    c=child(12)
    c.display()