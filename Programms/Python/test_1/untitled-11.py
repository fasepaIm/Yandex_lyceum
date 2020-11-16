for k in range(int(input())):
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    k = (min(a) + max(a)) / 3
    m = 2 * k
    print(min(a), max(a))
    b = input().split()
    for i in range(len(b)):
        b[i] = int(b[i])
    print(' '.join(str(i) for i in b if k <= i <= m))