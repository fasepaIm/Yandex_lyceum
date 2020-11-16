c = []
for i in range(int(input())):
    a = input()
    b = []
    while a != '*':
        b.append('-'.join([j for j in a.split()]))
        a = input()
    f = ('-'.join(j for j in b))
    c.insert(0, f)
d = ', '.join(i for i in c)
print(d)