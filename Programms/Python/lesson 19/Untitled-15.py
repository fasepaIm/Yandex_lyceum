def tic_tac_toe(field):
    n = ''
    for i in field:
        if i[0] == i[1] == i[2] != '-':
            print(f'{i[0]} win')
            return None
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] != '-':
            print(f'{field[0][i]} win')
            return None
    if field[0][0] == field[1][1] == field[2][2] != '-':
        print(f'{field[0][0]} win')
        return None
    if field[0][2] == field[1][1] == field[2][0] != '-':
        print(f'{field[0][2]} win')
        return None
    print('draw')