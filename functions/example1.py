#sum the digit of the number till the no. of digit becomes 1
def getlength(num):
    len=0
    while(num!=0):
        len+=1
        num=num//10
    return len

def sumofdigit(num):
    sum=0
    while(num!=0):
        temp=num%10
        sum=sum+temp
        num=num//10
    return sum

if __name__=='__main__':
    num=int(input("Enter the number: "))
    while(getlength(num)!=1):
        num=sumofdigit(num)
    print(num)