a,b,c,d = map(int,input().split())
m1 = (a*3)/10
m2 = a - ((a/250)*c)
misha = max(m1,m2)
v1 = (b*3)/10
v2 = b - ((b/250)*d)
vasya = max(v1,v2)

if misha < vasya:
    print("Vasya")
elif misha > vasya:
    print("Misha")
else:
    print("Tie")
