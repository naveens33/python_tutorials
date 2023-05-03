"""
Segregate 0s and 1s
"""

li = [0,1,0,1,1,0]
print(sorted(li))


li = [0,1,0,1,1,0]
count = li.count(0)
ans = []
for i in range(count):
    ans.append(0)

for i in range(len(li)-count):
    ans.append(1)

print(ans)

li = [0,1,0,1,1,0]

count = 0
for i in li:
    if i == 0:
        count+=1

ans = []
for i in range(count):
    ans.append(0)

for i in range(len(li)-count):
    ans.append(1)

print(ans)

def seg(li, size):
    left =  0
    right = size-1

    while left < right:
        while li[left] == 0 and left < right:
            left+=1

        while li[right] == 1 and left < right:
            right -=1

        if left < right:
            li[left] = 0
            li[right] = 1
            left+=1
            right-=1

    return li


li = [0,1,0,1,1,0]
print(seg(li, len(li)))

