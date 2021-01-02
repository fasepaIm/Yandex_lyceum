x1, y1, width1, height1 = [int(i) for i in input().split()]
x2, y2, width2, height2 = [int(i) for i in input().split()]

def some_shit(x11, x12, x21, x22):
    return x21 <= x11 <= x22 or x11 <= x21 <= x12

if some_shit(x1, x1 + width1, x2, x2 + width2) and some_shit(y1, y1 + height1, y2, y2 + height2):
    print('YES')
else:
    print('NO')
