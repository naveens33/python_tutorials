if __name__=='__main__':
    pass
'''
    for i in range(10,0,-1):
        print(i)
'''
"""
    balance=1250
    minimumbalance=100
    withdraw=int(input("Enter th amount: "))
    if (balance<withdraw):
        print("Isufficient Balance")
    else:
        if((balance-withdraw)<minimumbalance):
            print("u have to pay minimum balance in 5days")
        currentbalance=balance-withdraw
        print("The Current Balance is "+str(currentbalance))
"""

'''
    i=0
    while(i<3):
        i+=1
    else:
        print(i)
'''

'''
    for a in range(1,100):
        count=0
        for i in range(1, int(a / 2)+1):
            if (a % i == 0):
                count += 1
        if (count==1):
            print(a)
'''

'''
    a=16
    count=0
    for i in range(1,int(a/2)):
        if(a%i==0):
            count+=1
    if(count>1):
        print("Not a Prime Number")
    else:
        print("Prime Number")
'''

'''
    for i in range(1999,2100):
        if((i%3==0)or(i%19==0)):
            print("{0} is divisible by either 3 or 19".format(i))
'''

'''
    i=1999
    while(i<2100):
        if((i%3==0)or(i%19==0)):
            print("{0} is divisible by either 3 or 19".format(i))
        i=i+1
'''

'''
    i=10
    while(i>0):
        print(i)
        i-=1
'''

'''
    a=6;
    b=7
    c=a+b
    print("Addition of {0} and {1} is {2}".format(a,b,c))
'''

'''
    year=int(input("Enter the Year: "))
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                print(str(year)+" is Leap Year")
            else:
                print("{0} is Not Leap Year".format(year))
        else:
            print("Leap Year")
    else:
        print("Not Leap Year")
'''

'''
    age=int(input("Enter the Age"))
    if age>=18:
        pan =input("Pan Card status")
        if pan=="Yes":
            print("Eligible")
        elif pan=="No":
            print("Apply Pan first")
        else:
            print("Invalid value")
    else:
        print("Not Eligible")

'''

'''
    a=4
    b=2
    c=3
    #if((a<b) & (a<c)): TRUE & TRUE = TRUE, TRUE & FALSE = FALSE 
    if((a<b) and (a<c)):
        print(str(a)+" is smaller")
    elif((b<a) and (b<c)):
        print(str(b)+" is smaller")
    else:
        print(str(c)+" is smaller")

'''

'''
    a=int(input("Enter the number: "))
    if(a%3==0):
        print(str(a)+" is divided by 3")
    else:
        print(str(a)+" is not divided by 3")
'''
