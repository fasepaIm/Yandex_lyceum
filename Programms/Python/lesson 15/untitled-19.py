b = []
c = []
f = 0
a = [i for i in input().split(',')]
for i in a:
    c = i
    if '_' in i:
        c = i[:i.find('_')] + i[i.find('_') + 1:]
    if not c.isalnum():
        b.append(i)
for i in b:
    if len(i) > f:
        f = len(i)
b.sort()
for i in b:
    print((' ' * (f - len(i))) + i)