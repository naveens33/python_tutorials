if __name__=='__main__':
    #If Else example
    firstnumber, secondnumber=5,6
    if(firstnumber<secondnumber):
        print("firstnumber is lesser than secondnumber")
    else:
        print("secondnumber is lesser than firstnumber")

    print(False & True)
    # Else If example
    a,b,c=6,7,1
    if(a<b and a<c):
        print("a is smaller")
    elif(b<a and b<c):
        print("b is smaller")
    else:
        print("c is smaller")

    # Nested If example
    num = float(input("Enter a number: "))
    if num >= 0:
        if num == 0:
            print("Zero")
        else:
            print("Positive number")
    else:
        print("Negative number")

    # Example
    # Python program to check if the input year is a leap year or not
    year = int(input("Enter a year: "))

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))

    # while loop
    count = 0
    while (count < 3):
        count = count + 1
        print("Hello Hi")

    # combining else with while
    count = 0
    while (count < 3):
        count = count + 1
        print("Hello Hi")
    else:
        print("In Else Block")

    # Single statement while block
    #count = 0
    #while (count == 0): print("Hello Hi")

    # Iterating over a String
    s = "Hello World"
    for i in s:
        print(i)

    # Program to check Armstrong numbers in certain interval

    lower = 100
    upper = 2000

    # To take input from the user
    # lower = int(input("Enter lower range: "))
    # upper = int(input("Enter upper range: "))

    for num in range(lower, upper + 1):

        # order of number
        order = len(str(num))

        # initialize sum
        sum = 0

        # find the sum of the cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp = temp/10

        if num == sum:
            print(num)

    # Python program to find the factorial of a number provided by the user.

    # change the value for a different result
    num = 7

    # uncomment to take input from the user
    # num = int(input("Enter a number: "))

    factorial = 1

    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)

    # Python program to display all the prime numbers within an interval

    # change the values of lower and upper for a different result
    lower = 900
    upper = 1000

    # uncomment the following lines to take input from the user
    # lower = int(input("Enter lower range: "))
    # upper = int(input("Enter upper range: "))

    print("Prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)