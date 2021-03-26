'''
def sample(i):
    print(i)
    sample(i+1)

sample(0)
'''

# Factorial of 5 -> 1*2*3*4*5

'''
n = 3
ans = 1
for i in range(1, n+1):
    ans*=i
print(ans)
'''


# Find Factorial of 5 -> 1*2*3*4*5 in recursive function
# 1. Calling the function
# 2. Where to break it

def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)


print(f(3))
