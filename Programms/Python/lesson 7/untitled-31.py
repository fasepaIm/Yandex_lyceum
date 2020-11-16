c = int(input())
a = 0
kupil = 0
b = 0
prodal = 0
while c != 0:
    c1 = int(input())
    if c1 == 0:
        break
    elif c1 > c and kupil == 0:
        a = c1
        kupil = c1
        continue
    elif c1 > c:
        c = c1
    elif c1 < c:
        c = c1
        if a != 0 and c1 != a and prodal == 0:
            b = c1
            prodal = 1
            continue
print(kupil, b, b - kupil)