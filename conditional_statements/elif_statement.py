if __name__=='__main__':
    a = int(input('Enter the value for a: '))
    b = int(input('Enter the value for b: '))
    c = int(input('Enter the value for c: '))

    if a>b and a>c:
        print("a is bigger")
    elif b>a and b>c:
        print("b is bigger")
    else:
        print("c is bigger")
