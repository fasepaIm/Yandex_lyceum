a = input()
b = [0]
c = [0]
for i in range(len(a)):
    if b[-1] != a[i]:
        b.append(a[i])
        c.append(1)
    if b[-1] == a[i]:
        c[-1] += 1
for i in range(1, len(b)):
    print(c[i] - 1, b[i])