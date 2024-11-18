t = int(input())
for i in range(t):
    l1 = []
    n = int(input())
    l = list(map(int, input().split()))
    y = [l[i] for i in range(len(l))]
    y.sort()
    max1 = y[len(y) - 1]
    for j in range(len(l)):
        if l[j] == max1:
            b = l[j] - y[len(y) - 2]
            l1.append(b)
        else:
            b = l[j] - max1
            l1.append(b)
    for k in range(len(l1)):
        print(l1[k], end=' ')
    print()
