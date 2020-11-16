for i in range(int(input())):
    a = [int(i) for i in input().split()]
    b = [0]
    while len(a) != 0:
        if a[0] >= a[-1] and b[0] == 0:
            b.append(a[0])
            a.pop(0)
            del b[0]
        elif a[-1] >= a[0] and b[0] == 0:
            b.append(a[-1])
            a.pop(-1)
            del b[0]
        elif a[0] >= a[-1] and a[0] <= b[-1]:
            b.append(a[0])
            a.pop(0)
        elif a[-1] >= a[0] and a[-1] <= b[-1]:
            b.append(a[-1])
            a.pop(-1)
        else:
            break
    if len(a) == 0:
        print(' '.join(str(b).split(', '))[1:-1])
    else:
        print('НЕТ')
    del b[:]