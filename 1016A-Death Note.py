n, m = map(int, input().split())
a = list(map(int, input().split()))
extra = 0   
for i in range(n):
    count = 0      # for page no
    if extra > a[i]:
        extra -= a[i]
        a[i] = 0
    elif extra > 0:
        count += 1
        a[i] -= extra
        extra = 0
    if a[i]:
        count += a[i] // m
        extra = m - a[i] % m
    print(count)
