def line(s, t):
    x, y = t.split(';')
    s = s.split('x')
    k, zn = float(s[0]), s[-1][0]
    b = float(s[-1][1:])
    if zn == '+':
        if k * float(x) + b == float(y):
            print('True')
            return None
        else:
            print('False')
            return None
    else:
        if k * float(x) - b == float(y):
            print('True')
            return None
        else:
            print('False')
            return None