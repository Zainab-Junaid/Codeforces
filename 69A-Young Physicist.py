t = int(input())
sumx = sumy = sumz = 0
for _ in range(t):
    x,y,z = map(int,input().split())
    sumx += x
    sumy += y
    sumz += z
if sumx == 0 and sumy == 0 and sumz == 0:
    print('YES')
else:
    print('NO')
