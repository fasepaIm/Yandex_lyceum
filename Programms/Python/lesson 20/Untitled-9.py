def first_help(lol):
    zaz = {
        'A': '1',
        'B': '2',
        'C': '3',
        'D': '4',
        'E': '5',
        'F': '6',
        'G': '7',
        'H': '8',   
    }
    return (int(zaz[lol[0]]), int(lol[-1]))


def second_help(pip):
    zaz = {
        '1': 'A',
        '2': 'B',
        '3': 'C',
        '4': 'D',
        '5': 'E',
        '6': 'F',
        '7': 'G',
        '8': 'H'
    }
    a = pip
    for i in range(len(a)):
        a[i] = zaz[a[i][0]] + a[i][-1]
    a.sort()
    return a


def possible_turns(cell):
    a = first_help(cell)
    z = []
    if a[0] + 1 <= 8 and a[-1] + 2 <= 8:
        z.append(str(a[0] + 1) + str(a[-1] + 2))
    if a[0] - 1 > 0 and a[-1] + 2 <= 8:
        z.append(str(a[0] - 1) + str(a[-1] + 2))
    if a[0] + 2 <= 8 and a[-1] + 1 <= 8:
        z.append(str(a[0] + 2) + str(a[-1] + 1))
    if a[0] + 2 <= 8 and a[-1] - 1 > 0:
        z.append(str(a[0] + 2) + str(a[-1] - 1))
    if a[0] - 1 > 0 and a[-1] - 2 > 0:
        z.append(str(a[0] - 1) + str(a[-1] - 2))
    if a[0] + 1 <= 8 and a[-1] - 2 > 0:
        z.append(str(a[0] + 1) + str(a[-1] - 2))
    if a[0] - 2 > 0 and a[-1] + 1 <= 8:
        z.append(str(a[0] - 2) + str(a[-1] + 1))
    if a[0] - 2 > 0 and a[-1] - 1 > 0:
        z.append(str(a[0] - 2) + str(a[-1] - 1))
    return second_help(z)