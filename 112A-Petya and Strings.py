def string(s1,s2):
    if s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    return -1

s1 = input().lower()
s2 = input().lower()
result = string(s1,s2)
print(result)
