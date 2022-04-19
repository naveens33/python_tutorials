#palindrome or not

word = "madam"
rev = word[::-1]
if word == rev:
    print("Palindorme")
else:
    print("not Palindrome")

for i in range(len(word)//2):
    if word[i]!=word[len(word)-i-1]:
        print("Not Palindorme")
        break
else:
    print("Palindorme")
