n = int(input())
l = list(map(int,input().split()))
l.sort()
if n == 0 :
    print(0)
elif n in l:
    print(1)
else:
    summ = 0
    count = 0
    for i in range(len(l)-1,-1,-1):
        summ += l[i]
        count += 1
        if summ >= n:
            print(count)
            break
    else:
        print(-1)
    
         
