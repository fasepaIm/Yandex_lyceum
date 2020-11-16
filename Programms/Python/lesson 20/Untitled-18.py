def check_pin(pinCode):
    test = 0
    a = pinCode.split('-')
    d = 0
    for i in range(1, int(a[0]) + 1):
        if int(a[0]) % i == 0:
            d += 1
        if d > 2:
            break
    if d == 2:
        test += 1
    b = []
    s = []
    for i in a[1]:
        for j in i:
            s.append(j)
            b.append(j)
    b.reverse()
    if s == b:
        test += 1
    z = 2
    step = 1
    while z ** step <= int(a[-1]):
        if int(a[-1]) == z ** step:
            test += 1
        step += 1
    if test == 3:
        return 'Корректен'
    else:
        return 'Некорректен'