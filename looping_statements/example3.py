# Palindrom or not 1331

if __name__ == '__main__':
    num = int(input("Enter the number: "))
    copy = num
    rev = 0
    while (num != 0):
        temp = num % 10
        rev = (rev * 10) + temp
        num = num // 10
    if rev == copy:
        print("Its is a palindrome")
    else:
        print("Not palindrome")

'''
num=123
rev=0
-----------
123!=0 True
temp=123%10
rev=(0*10)+3
num=123//10
------------
num=12
rev=3
-------------
12!=0 True
temp=12%10
rev=(3*10)+2
num=12//10
-------------
num=1
rev=32
--------------
1!=0 True
temp=1%10
rev=(32*10)+1
num=1//10
---------------
num=0
rev=321
--------------
0!=0 False
-----------------
'''
