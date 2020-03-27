# else statement for while and for loop
if __name__ == '__main__':
    num = 18
    for i in range(2,num//2):
        if num%i == 0:
            print("Not Prime number")
            break
    else:
        print("Prime number")