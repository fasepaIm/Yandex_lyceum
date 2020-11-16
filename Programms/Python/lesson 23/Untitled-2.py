coffe = {
    'Эспрессо': [1, 0, 0],
    'Капучино': [1, 3, 0],
    'Маккиато': [2, 1, 0],
    'Кофе по-венски': [1, 0, 2],
    'Латте Маккиато': [1, 2, 1],
    'Кон Панна': [1, 0, 1]
}


def choose_coffee(*choose):
    global ingredients, coffe
    for i in choose:
        skip = True
        for j in range(3):
            if ingredients[j] < coffe[i][j]:
                skip = False
                break
        if skip:
            for j in range(3):
                ingredients[j] -= coffe[i][j]
            return i
    if not skip:
        return 'К сожалению, не можем предложить Вам напиток'