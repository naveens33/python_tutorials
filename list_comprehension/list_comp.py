# List Comprehension

# newlist = [expression/element for element in list if condition]

li = []
s = "Courage the dog"
for c in s:
    li.append(c)
print(li)

x = [c for c in s]
print(x)

s = []
li = [34, 39, 45]
for i in li:
    s.append(i * 2)
print(s)

x = [i * 2 for i in li]
print(x)

li = []
s = "courage the dog"
for c in s:
    if c in "aeiou":
        li.append(c)
print(li)

x = [c for c in s if c in "aeiou"]
print(x)

li = []
for i in range(500, 1000):
    if i % 13 == 0 and i % 19 == 0:
        li.append(i)
print(li)

x = [i for i in range(500, 1000) if i % 13 == 0 if i % 19 == 0]
print(x)

x = [i for i in range(0, 10) if i % 2 == 0 or i % 3 == 0]
print(x)

age = 17
if age >= 18:
    print("Elig")
else:
    print("Not Elig")

# Terinary operator - Java/C#
# Condition Expression - Python
# var = <true_exp> if condition else <false_exp>
x = "Elig" if age >= 18 else "Not Elig"
print(x)

li = [56, 57, 58, 59, 61]
# [even,odd,even,odd,odd]
x = ["Even" if i % 2 == 0 else "Odd" for i in li]
print(x)

num = 78
x = "Even" if num % 2 == 0 else "Odd"
print(x)
