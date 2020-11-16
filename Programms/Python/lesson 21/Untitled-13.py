money = {}


def get_transactions(t):
    global money
    if t == 'print_it':
        for i in money:
            print(f'{money[i][-1]} {i} {money[i][0]}')
    else:    
        a = t.split('-')
        b = a[-1].split(':')
        if b[0] in money:
            x = b[0]
            money[x][0] += int(b[-1])
            money[x][-1] += 1
        else:
            x = b[0]
            money[x] = [int(b[-1]), 1]