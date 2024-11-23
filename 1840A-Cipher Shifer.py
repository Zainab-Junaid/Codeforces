t = int(input())
for  _ in range(t):
    n = int(input())
    s = input()
    a = 0
    while a < n:
        for i in range(a+1,n):
            if s[a] == s[i]:
                print(s[a],end='')
                a = i+1
                break
    print()
            
   
        
