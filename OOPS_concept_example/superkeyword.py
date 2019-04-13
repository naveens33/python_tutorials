class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("C")

if __name__=='__main__':
    obj=C()