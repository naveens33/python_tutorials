#Sum of n number - while loop
if __name__=='__main__':
    n=int(input("Enter the value for n: "))
    i=1
    sum=0
    while(i<=n):
        sum=sum+i
        i=i+1
    print(sum)