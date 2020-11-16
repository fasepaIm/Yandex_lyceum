a = []
xxx = '*_*'
new = '-/-'
for i in range(int(input())):
    c = [j for j in input().split(',')]
    a.append(c)
b = []
for i in range(len(a)):
    for j in range(len(a[i])):
        if xxx in a[i][j]:
            z = a[i][j].split(xxx)
            m = ','.join(z)
            a[i][j] = m
        if new in a[i][j]:
            z = a[i][j].split(new)
            m = '\\n'.join(z)
            a[i][j] = m
for i in range(int(input())):
    c = [j for j in input().split(',')]
    b.append(c)
for i in b:
    print(a[int(i[0])][int(i[-1])])