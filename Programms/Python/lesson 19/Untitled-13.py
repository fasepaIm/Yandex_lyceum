def squared():
    cnt = []
    str0 = []
    for i in range(11, 101):
        if i % 10 != 0:
            str0.append(str(i ** 2).ljust(4, ' '))
        else:
            n = str0.copy()
            cnt.append(n)
            str0.clear()
    for i in cnt:
        print(' '.join(i).rstrip())