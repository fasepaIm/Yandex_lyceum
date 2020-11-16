a = []
b = []
d = 0
for i in range(int(input())):
    a.append([j for j in input().split()])
c = int(input())
for i in a:
    if len(i) > c:
        b.append(int(i[c - 1]) - (int(i[c - 1]) * (int(i[-1]) / 100)))
for i in b:
    d += i
if d - int(d) == 0:
    d = int(d)
print(d)