l1=[1,2,3]
l2=[4,5,6]

ans = []
for i in l1:
    for j in l2:
        ans.append(i*j)

print(ans)


ans = [i*j for i in l1 for j in l2]
print(ans)