a = 1
c = 0
d = 0
for i in range(1, 10000):
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            c += j
    for t in range(1, c // 2 + 1):
        if c % t == 0:
            d += t
    if i == d and i != c:
        if a % 2 != 0:
            print(i, c)
        a += 1
    c = 0
    d = 0