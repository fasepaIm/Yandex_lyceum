a = []
b = []
c = []
e = []
d = 0
m = ''
for i in range(int(input())):
    f = [int(s) for s in input().split()]
    f.sort()
    a.append(f)
for i in a:
    b.append(int((i[(len(i) - 1) // 2])))
print(' '.join(str(b).split(', '))[1:-1])
for i in a:
    for t in i:
        if i.count(t) > d and t != ' ':
            d = i.count(t)
            m = int(t)
    c.append(m)
    d = 0
    m = ''
print(' '.join(str(c).split(', '))[1:-1])
b.sort()
print(int((b[(len(b) - 1) // 2])))
for i in c:
    if c.count(i) > d and i != ' ':
        d = c.count(i)
        m = i       
print(m)
d = 0
m = '' 
for i in a:
    for j in i:
        if j != ' ':
            e.append(int(j))
e.sort()
print(int((e[(len(e) - 1) // 2])))
for i in e:
    if e.count(i) > d and i != ' ':
        d = e.count(i)
        m = i
print(m)