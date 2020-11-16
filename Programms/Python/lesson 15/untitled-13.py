a = [int(i) for i in input().split()]
a.sort()
c = 0
d = 0
for i in a:
    if a.count(i) > c and i != ' ':
        c = a.count(i)
        d = i
m = a[(len(a) - 1) // 2]
print(m, d)