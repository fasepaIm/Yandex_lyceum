b = 0
a = [float(i) for i in input().split()]
a.sort()
m = len(a)
for i in a:
    b += i
b /= m
if m % 2 != 0:
    c = float(a[(m - 1) // 2])
else:
    c = float((a[m // 2 - 1] + a[m // 2]) / 2)
print(b, c)