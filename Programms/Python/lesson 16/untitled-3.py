c = []
a, b = int(input()), int(input())
for i in range(a):
    d = []
    for j in range(b):
        d.append(input())
    c.append(d)
for i in range(a):
    for j in range(b):
        print(c[i][j], end='\t')
    print()