n,h = map(int,input().split())
a = list(map(int,input().split()))
count = 0
for i in range(len(a)):
    if a[i] <= h:
        count+= 1
    else:
        count+= 2
print(count)
