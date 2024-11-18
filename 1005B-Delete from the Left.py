s1 = input()
s2 = input()
z1 = s1[::-1]
z2 = s2[::-1]
summ = len(s1)+len(s2)
a = max(len(s1),len(s2))
count = 0
if a == len(s1):
    for i in range(len(z2)):
        if z1[i]== z2[i]:
            count += 1
        else:
            break
    if count >0:
        d = abs((count +count)-summ)
        print(d)
    else:
        print(summ)
else:
    for i in range(len(z1)):
        if z1[i]== z2[i]:
            count += 1
        else:
            break
    if count >0:
        d = abs((count +count)-summ)
        print(d)
    else:
        print(summ)
        
        
