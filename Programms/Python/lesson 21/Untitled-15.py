def diet(eat):
    global food
    normal = 0
    meals = eat.split(', ')
    norma = len(meals) // 2
    for i in meals:
        if i not in food['диетическое']:
            normal += 1
    if normal > norma:
        return 'Не ешь столько, По!'
    else:
        return 'Так держать, Воин Дракона!'