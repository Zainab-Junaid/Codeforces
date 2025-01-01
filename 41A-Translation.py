def trans(s,t):
    t1=''
    for i in range(len(s)-1,-1,-1):
        t1+= s[i]
    if t1 == t:
        return "YES"
    return "NO"
s = input()
t = input()  
result = trans(s,t)
print(result)
