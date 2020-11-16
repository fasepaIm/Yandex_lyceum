def equation(a, b):
    x = float(a.split(";")[0])
    x2 = float(b.split(";")[0])
    y = float(a.split(";")[1])
    y2 = float(b.split(";")[1])
    if x - x2 == 0:
        print(0.0)
        return None
    k = (y - y2) / (x - x2)
    b = y2 - k * x2
    if k == 0:
        print(b)
        return None
    print(k, b)