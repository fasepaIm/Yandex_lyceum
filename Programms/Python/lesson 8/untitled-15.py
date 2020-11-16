n = int(input())
a = 0
x = 0
for i in range(1, n + 1):
    b = i
    for j in range(1, i + 1):
        if i % j == 0:
            x += 1
    if x == 2 and i < n:
        print(i)
    x = 0