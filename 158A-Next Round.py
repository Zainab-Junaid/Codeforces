def round(l,k):
    count = 0
    if set(l) == {0}:
        return 0
    for i in range(len(l)):
        if l[i] >= l[k-1] and l[i] != 0:
            count+= 1
    return count

n,k = map(int,input().split())
l = list(map(int,input().split()))
result = round(l,k)
print(result)
