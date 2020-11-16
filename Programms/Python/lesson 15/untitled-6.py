a = [str(i) for i in input().split()]
for i in a:
    b = a.index(i)
    a[b] = (str('-'.join(str(a[b])))).upper()
for i in a:
    print(i, end=' ')