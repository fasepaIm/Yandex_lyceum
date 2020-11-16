a = []
d = ''
f = '-'
rew = int(input())
for i in range(rew):
    a.append(input())
for i in a:
    if 'ooo' in i:
        f = 'o'
        break
    if 'xxx' in i:
        f = 'x'
        break
if f == '-':
    for i in range(rew):
        for j in range(rew):
            d += a[j][i]
        if 'ooo' in d:
            f = 'o'
            break
        if 'xxx' in d:
            f = 'x'
            break
        d = ''
print(f)