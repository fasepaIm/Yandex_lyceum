n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] < a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
for i in a:
    print(i)