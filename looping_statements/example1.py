# Sum of n numbers
if __name__ == '__main__':
    num = int(input("Enter the number: "))
    i = 1
    sum = 0
    while i <= num:
        sum = sum + i
        i = i + 1
    print(sum)

"""
num=3
i=1
sum=0
-------------
1<=3 True
sum=0+1
i=1+1
-------------
sum=1
i=2
-------------
2<=3 True
sum=1+2
i=2+1
-------------
sum=3
i=3
--------------
3<=3 True
sum=3+3
i=3+1
-------------
sum=6
i=4
------------
4<=3 False
-------------
print(sum)
"""