s = list("testss")
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i] == s[j]:
            s[i] = 0
            s[j] = 0
            break
print(s)
count =0
for c in s:
    if c !=0:
        count+=1

if count <2:
    print("Pali")
else:
    print("Not Pali")