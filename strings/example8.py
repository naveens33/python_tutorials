# Permutation of string
def per(s,ans):
    if len(s) == 0:
        print(ans)

    for i in range(len(s)):
        ch = s[i]
        rest = s[:i]+s[i+1:]
        per(rest, ans+ch)


s = "ABC"
per(s,"")