a = int(input())
b = int(input())
c = []
d = []
for i in range(a):
    c.append(input())
for i in range(0, a, 2):
    d.append(c[i])
c = []
for i in d:
    s = ''
    for j in range(-1, b + 1, 2):
        if j != -1:
            s += i[j - 1]
    c.append(s)
for i in c:
    print(i)