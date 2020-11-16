n = int(input())
x = 1
i = 1
k = 0
while i <= n:
    for j in range(i, i + x):
        if i > n:
            break
        else:
            print(i, end=' ')
            i += 1
            k = k + 1
        if k == x:
            print()
            x += 1
            k = 0