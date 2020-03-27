# else statement for while and for loop
if __name__ == '__main__':
    '''
    # Prime number program
    # Its not necessary to go complete iteration
    num = int(input("Enter the number: "))
    i=2
    count=0
    while(i<=num//2):
        if num%i==0:
            count+=1
        i+=1

    if count > 0:
        print("Its is not a prime number")
    else:
        print("Its a prime number")
    '''

    '''
    # while loop
    num = int(input("Enter the number: "))
    i=2
    while i<num//2:
        if num%i==0:
            print("Its not prime number")
            break
        i+=1
    else:
        print("Its a prime number")
    '''

    num = 18
    for i in range(2,num//2):
        if num%i == 0:
            print("Not Prime number")
            break
    else:
        print("Prime number")