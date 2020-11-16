a = []
b = []
for i in range(int(input())):
    a.append(input())
for i in a:
    d = i.split()
    if d[0] == 'Кто' and d[1] == 'последний?':
        b.append(i[i.find('-') + 2:-1])
    if d[0] == 'Я' and d[1] == 'только' and d[2] == 'спросить!':
        m = d[5:]
        b.insert(0, str(m)[2:-3])
    if d[0] == 'Следующий!':
        if len(b) == 0:
            print('В очереди никого нет.')
        else:
            print('Заходит', b[0] + '!')
            del b[0]