d = []
for _ in range(5):
    l = list(map(int,input().split()))
    d.append(l)
for i in range(5):
    for j in range(5):
        if d[i][j] == 1:
            row = i
            colm = j
result = abs((row+1)-3) + abs((colm+1)-3)
print(result)
