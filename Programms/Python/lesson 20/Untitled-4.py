def print_document(pages):
    n = 0
    for i in pages:
        a = i.split(' ', 1)
        if a[0] != 'Секретно':
            print(i)
        else:
            print('Дальнейшие материалы засекречены')
            n = 1
            break
    if n == 0:
        print('Напечатано без купюр')