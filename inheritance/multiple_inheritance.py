class Parent1:
    def display(self):
        print("Parent1")

class Parent2:
    def display(self):
        print("Parent2")

class Child(Parent2,Parent1):
    def display3(self):
        print("Child")

if __name__=='__main__':
    c=Child()
    c.display()