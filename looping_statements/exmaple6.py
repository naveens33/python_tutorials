#Triangle pattern *
if __name__=='__main__':
    n=6
    for i in range(1,n):
        for k in range(i,n-1):
            print(' ',end="")
        for j in range(i):
            print('*',end="")
        for j in range(i-1):
            print('*',end="")

        print()

