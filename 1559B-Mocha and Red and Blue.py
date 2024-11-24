def what_to_write(s):
    count=0
    i=0
    for c in range(len(s)):
        if s[i] == '?' and i == 0 and len(s)!=1:
            if s[i + 1] == 'B':
                s[i] = 'R'
            elif s[i + 1] == 'R':
                s[i] = 'B'
            else:
                for k in range(len(s)):
                    if s[k] != '?':
                        count += 1
                        if s[k] == 'B':
                            v = 'B'
                            for u in range(k - 1, -1, -1):
                                if v == 'B':
                                    v = 'R'
                                else:
                                    v = 'B'
                                s[u] = v
                            break
                        else:
                            v = 'R'
                            for u in range(k - 1, -1, -1):
                                if v == 'B':
                                    v = 'R'
                                else:
                                    v = 'B'
                                s[u] = v
                            break
                if count == 0:
                    s[i] = 'B'
        elif s[i]=='?' and i!=len(s)-1 and i!=0:
            if (s[i+1]=='R' and s[i-1]=='R') or (s[i+1]=='?' and s[i-1]=='R'):
                s[i]='B'
            elif (s[i+1]=='B' and s[i-1]=='B') or (s[i+1]=='?' and s[i-1]=='B'):
                s[i]='R'
            elif (s[i+1]=='B' and s[i-1]=='R') or (s[i+1]=='R' and s[i-1]=='B'):
                s[i]='R'
        elif s[i] == '?' and i == len(s) - 1:
            if s[i-1]=='B':
                s[i]='R'
            else:
                s[i]='B'
        i+=1
    return s
t=int(input())
for i in range(t):
    n=int(input())
    s=list(input())
    l=what_to_write(s)
    for j in range(len(l)):
        print(l[j],end='')
    print()
