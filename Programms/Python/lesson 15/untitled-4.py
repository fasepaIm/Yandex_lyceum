c = 0
a = [int(i) for i in input().split()]
b = [int(j) for j in input().split()]
for i in range(b[0], b[1] + 1):
    c += a[i] ** 2
print(c)