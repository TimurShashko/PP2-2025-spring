def permutate(s,ans=""):
    if len(s)==0:
        print(ans)
        return ""
    for i in range (0,len(s)):
        a=s[i]
        s_a=s[:i]+s[i+1:]
        permutate(s_a, a+ans)

permutate("abc")
print("")