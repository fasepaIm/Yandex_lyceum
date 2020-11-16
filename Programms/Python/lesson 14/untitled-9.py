b = []
a = [i for i in input().split()]
for i in range(int(max(a))):
    c = 0
    p = '*'
    for j in a:
        if int(j) > 0:
            p += '*'
        else:
            p += ' '
        a[c] = int(j) - 1
        c += 1
    p += '*'
    b.append(p)
b.append('*' + len(a) * ' ' + '*')
b.append((len(a) + 2) * '*')
for i in range(len(b) - 1, -1, -1):
    print(b[i])