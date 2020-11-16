def find_mountain(heightsMap):
    row = 0
    cal = 0
    z = 0
    for i in range(len(heightsMap)):
        a = max(heightsMap[i])
        if a > z:
            z = a
            row = i
            cal = heightsMap[i].index(a)
    return (row, cal)