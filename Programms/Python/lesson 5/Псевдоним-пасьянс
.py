tut = int(input())
while tut > 0:
    v = int(input())
    if 0 < v <= tut and v <= 3:
        tut -= v
        print(tut)
    else:
        print(tut)