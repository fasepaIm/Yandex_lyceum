def late(now, classes, bus):
    z = 0
    now = now.split(':')
    classes = classes.split(':')
    while bus[0] < 5:
        del bus[0]
        if len(bus) == 0:
            return 'Опоздание'
    m = bus[0]
    ch = int(now[0])
    minutes = int(now[-1]) + (m - 5) + 15
    if minutes >= 60:
        ch += 1
        minutes -= 60
    if ch > int(classes[0]) or (minutes > int(classes[-1]) and
                                ch == int(classes[0])):
        return 'Опоздание'
    else:
        for i in range(len(bus) - 1, -1, -1):
            m = bus[i]
            ch = int(now[0])
            minutes = int(now[-1]) + (m) + 15
            if minutes >= 60:
                ch += 1
                minutes -= 60
            if (minutes <= int(classes[-1]) and ch <= int(classes[0]))\
                    or (minutes <= int(classes[-1]) and ch == int(classes[0]))\
                    or (ch < int(classes[0]) and minutes > int(classes[-1])):
                exitt = bus[i] - 5
                z = 1
                return f'Выйти через {exitt} минут'
    if z != 1:
        return 'Опоздание'