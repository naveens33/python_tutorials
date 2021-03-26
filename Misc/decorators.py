"""
function can be assigned to a attribute
where f1 and d two names are for the same function
"""


def f1():
    print("function 1")


d = f1
d()
'''
The next important fact is that we can delete either "d" or "f1" without deleting the function itself.
'''
del f1
d()


def make_pretty(func):
    func("Naveen")


@make_pretty
def ordinary(str):
    print(str)


ordinary


# defining a decorator
def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")

    return inner1


def function_to_be_used():
    print("This is inside the function !!")


function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()


# converting to decorator
def hello_decorator(func):
    def inner1():
        print("decorator- Hello, this is before function execution")
        func()
        print("decorator- This is after function execution")

    return inner1


@hello_decorator
def function_to_be_used():
    print("decorator- This is inside the function !!")


function_to_be_used()


# decorators with parameters
def decorators1(*args, **kwargs):
    def inner(func):
        print("Name is :" + kwargs["Name"])
        return func

    return inner


@decorators1(Name="Naveen")
def function_to_be_used1():
    print("Program completed")


function_to_be_used1()


# function with parameter
def decorator2(func):
    def addWelcome(sitename):
        return "Welcome to " + func(sitename)

    return addWelcome


@decorator2
def site(sitename):
    return sitename


print(site("www.google.com"))

def decorator2(*args,**kwargs):
    def addWelcome(func):
        print(kwargs["UserName"])
        return func
    return addWelcome


@decorator2(UserName="Naveen.S@gmail.com")
def site(sitename):
    return sitename

print(site("www.google.com"))

