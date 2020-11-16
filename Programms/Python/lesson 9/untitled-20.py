m, n = int(input()), int(input())
c = m + n
y = set()
for i in range(c):
    s = input()
    if s not in y:
        y.add(s)
    elif s in y:
        y.discard(s)
if len(y) > 0:
    print(len(y))
else:
    print('NO')