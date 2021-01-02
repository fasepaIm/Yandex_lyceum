from math import sqrt


x1, y1, r1 = [int(i) for i in input().split()]
x2, y2, r2 = [int(i) for i in input().split()]
if sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) <= r1 + r2:
    print('YES')
else:
  print('NO')
