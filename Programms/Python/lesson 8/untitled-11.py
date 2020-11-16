n = int(input())
a = 0
b = 0
c = 0
d = 0
for i in range(1, n + 1):
    k = int(input())
    for j in range(k):
        v = int(input())
        if a == 0:
            a = v
            b = i
        elif a != 0:
            if v < a:
                a = v
                b = i
    if a > c:
        d = b
        c = a
    a = 0
    b = 0
print(d, c)