#Find the even numbers from a range

li= [i for i in range(10) if i%2==0]
print(li)

#Find the numbers divisible by 13 and 19

'''
li=[]
for i in range(1000):
    if i % 13 == 0 and i % 19 == 0:
        li.append(i)
'''

li = [i for i in range(1000) if i%13==0 and i%19==0]
print(li)

#Nested If -  Find character which is vowel and it is upper case
sentence = "You are Awesome"
'''
li=[]
for c in sentence:
    if c in "aeiou" or c in "AEIOU":
        if c.isupper():
            li.append(c)
print(li)
'''
li = [c for c in sentence if c in "aeiou" or c in "AEIOU" if c.isupper()]
print(li)