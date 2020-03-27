# Swap Case without using method
text = "Process Finished With Exit Code 0"
result = ""
for i in range(len(text)):
    if text[i].isupper():
        result += text[i].lower()
    elif text[i].islower():
        result += text[i].upper()
    else:
        result += text[i]

print(result)


name = "Mr. Karthick BA. BL."
#print(name.swapcase())
ans = ""
for c in name:
    if c.isupper():
      ans =  ans+c.lower()
    else:
        ans = ans+c.upper()
print(ans)