m, n, k = int(input()), int(input()), int(input())
d = m + n + k
y1 = set()
y2 = set()
y3 = set()
for i in range(d):
    f = input()
    if f not in y1:
        y1.add(f)
    elif f in y1 and f not in y2:
        y2.add(f)
    elif f in y2:
        y3.add(f)
itog = y2 - y3
if len(itog) > 0:
    print(len(itog))
else:
    print('NO')