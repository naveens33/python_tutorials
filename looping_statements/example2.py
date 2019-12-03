#Sum of n number - for loop
if __name__=='__main__':
    n=int(input("Enter the value for n: "))
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print(sum)