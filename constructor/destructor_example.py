class Sample:

    def __init__(self):
        print("Constructor Called")

    def display(self):
        print("Hello, World!")

    def __del__(self):
        print("Destructor Called")

obj1 = Sample()
obj1.display()
obj2 = Sample()


