n = int(input())
s = input()
c1 = s.count('1')
c0 = s.count('0')
if c1 == c0:
    print(0)
else:
    print(abs(c1-c0))
