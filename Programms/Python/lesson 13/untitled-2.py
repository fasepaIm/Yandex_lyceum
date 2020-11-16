a = []
d = []
for i in range(int(input())):
    a.append(input())
    k = tuple(a)
for i in range(int(input())):
    b = int(input())
    d = []
    for j in range(b):
        c = int(input())
        d.append(k[c - 1])
    a = d
    k = tuple(a[:b])
for n in range(b):
    print(d[n])