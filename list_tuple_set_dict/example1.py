#Remove duplicate element in a list
li=[1,1,2,2,3,3]
s=set(li)
print(s)
li=list(s)
print(li)


li = [56, 49, 10, 49, 70, 56]
ans = []
for i in li:
    if i not in ans:
        ans.append(i)

print(ans)