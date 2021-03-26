#if in the list comprehension
sentence = "you are amazing"

li = []
'''
for c in sentence:
    if c in "aeiou":
        li.append(c)
print(li)
'''

li = [c for c in sentence if c in "aeiou"]
print(li)

