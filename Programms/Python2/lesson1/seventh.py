first_win = {
    'камень': ['ром', 'ножницы'],
    'ножницы': ['бумага', 'ром'],
    'бумага': ['камень', 'пират'],
    'ром': ['пират', 'бумага'],
    'пират': ['камень', 'ножницы']
}
first, second = input(), input()
if first == second:
    print('ничья')
elif second in first_win[first]:
    print('первый')
else:
    print('второй')
