f = []
for i in range(int(input())):
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c, d = min(a), max(a)
    print(c, d)
    c_ = (c + d) / 3
    d_ = (2 * (c + d)) / 3
    for i in b:
        if i > c_ and i < d_:
            f.append(i)
    print(' '.join(str(f).split(', '))[1:-1])
    f = []