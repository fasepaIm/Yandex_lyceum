a = int(input())
b = [[0] * a for i in range(a)]
for i in range(1, a):
    c = [j for j in input().split()]
    for j in range(i):
        b[i][j] = b[j][i] = int(c[j])
for i in b:
    print(' '.join(str(j) for j in i))