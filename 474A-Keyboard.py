h = input()
s = input()
l = 'qwertyuiopasdfghjkl;zxcvbnm,./'
if h == 'R':
    for i in range(len(s)):
        if s[i] == 'q':
            print('/',end='')
        else:
            ind = l.index(s[i])
            print(l[ind-1],end='')
else:
    for i in range(len(s)):
        if s[i] == '/':
            print('q',end='')
        else:
            ind = l.index(s[i])
            print(l[ind+1],end='')
