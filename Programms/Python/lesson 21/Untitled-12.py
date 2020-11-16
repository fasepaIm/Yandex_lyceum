bet = []


def do_bet(num, summ):
    if num <= 0 or num > 10 or summ == 0 or num in bet:
        print('Что-то пошло не так, попробуйте еще раз')
    else:
        bet.append(num)
        print(f'Ваша ставка в размере {summ} на лошадь {num} принята')