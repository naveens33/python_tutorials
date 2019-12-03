#Convert uppercase to lowercase and vice versa
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