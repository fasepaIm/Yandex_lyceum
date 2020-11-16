def hello(name):
    print(f'Здравствуйте, {name}! Вашу карту ищут...')


def search_card(name):
    global base
    if name in base:
        num = base.index(name) + 1
        print(f'Ваша карта с номером {num} найдена')
    else:
        print('Ваша карта не найдена')