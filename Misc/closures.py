#Nested function
'''
def A():
    def B():
        print("Hello")
    B()

A()
'''
'''
def A(msg):
    def B():
        print(msg)
    B()

A("Hello World")
'''
def A(msg):
    def B():
        print(msg)
    return B

fun  = A("Hello World")
fun()