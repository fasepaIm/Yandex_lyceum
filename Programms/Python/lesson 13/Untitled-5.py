a = []
c = 0
f = 0
for i in range(int(input())):
    a.append(input())
k = int(input())
for i in range(int(input())):
    d = []
    b = []
    s = 0
    for j in range(len(a)):
        c += 1
        if c == k and (f + c) - 1 <= len(a):
            f += c
            b.append(a[f - 1])
            c = 0
        elif (f + c) - 1 > len(a):
            f = 0
    f = 0
    for h in a:
        if h not in b:
            d.append(h)
#    for h in a:
#        if a.count(h) > 1 and h in b and s == 0:
#            d.append(h)
#            s = 1
    a = d
for i in a:
    print(i)