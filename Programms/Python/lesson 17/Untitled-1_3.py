lya = int(input())
children = {}
for i in range(lya):
    a = input().split()
    b = a[-1]
    a = [a[0] + ' ' + a[1]]
    if b in children:
        children[b] += a
    else:
        children[b] = a
for i in children:
    if len(children[i]) > 1:
        z = children[i]
        for k in range(len(z) - 1):
            for j in range(len(z) - 1 - k):
                if int(z[j][-2:]) > int(z[j + 1][-2:]):
                    z[j], z[j + 1] = z[j + 1], z[j]
                if int(z[j][-2:]) == int(z[j + 1][-2:]):
                    if z[j][:-2] > z[j + 1][:-2]:
                        z[j], z[j + 1] = z[j + 1], z[j]
        children[i] = z
for i in range(int(input())):
    a = input()
    if a in children:
        print(' '.join(children[a]))
    else:
        print()