side = "север"
side1 = "север"
moves = 0
short_moves = 0
c = 0
x, y = int(input()), int(input())
x1 = 0
y1 = 0
if x == x1 and y == y1 and c == 0:
    c = 1
    short_moves = moves
    side1 = side
    print(short_moves)
    print(side1)
moves = 1
a = input()
while a != "стоп" and (y1 != y or x1 != x):
    if a == 'вперёд': 
        if side == 'север':
            b = int(input())
            y1 += b
        elif side == 'юг':
            b = int(input())
            y1 -= b
        elif side == 'запад':
            b = int(input())
            x1 -= b
        elif side == 'восток':
            b = int(input())
            x1 += b
    elif a == 'налево':
        if side == 'север':
            side = 'запад'
        elif side == 'юг':
            side = 'восток'
        elif side == 'запад':
            side = 'юг'
        elif side == 'восток':
            side = 'север'
    elif a == 'направо':
        if side == 'север':
            side = 'восток'
        elif side == 'юг':
            side = 'запад'
        elif side == 'запад':
            side = 'север'
        elif side == 'восток':
            side = 'юг'
    elif a == 'разворот':
        if side == 'север':
            side = 'юг'
        elif side == 'юг':
            side = 'север'
        elif side == 'запад':
            side = 'восток'
        elif side == 'восток':
            side = 'запад'
    if x == x1 and y == y1 and c == 0:
        c = 1
        short_moves = moves
        side1 = side
        print(short_moves)
        print(side1)        
    else:
        a = input()
        moves += 1