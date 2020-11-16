def horizontal_reflection(zaz):  # функция ответственная за горизонтальное отражение
    gori = []          # переводит строки в список списков и затем переворачивает их
    for i in zaz:
        orr = []
        for j in i:
            orr.append(j)
        gori.append(orr)
    for i in range(a):
        gori[i].reverse()
    return gori


def vertical_reflection(tip):  # функция ответственная за вертикальное отражение
    vert = []                 # переворачивает список состоящий из строк
    for i in tip:
        vert.append(i)
    vert.reverse()
    return(vert)


def transpose(lsd):  # функция ответственная за транспонсирование
    trip = []  # создаётся список списков и в него поочереди добавляются
    st = []    # по одному элементу из каждой строки
    for i in range(a):
        trip.append([])
    for i in lsd:
        opt = []
        for j in i:
            opt.append(j)
        st.append(opt)
    for i in range(a):
        for j in range(a):
            trip[j].append(st[i][j])
    return trip


lol = []
a = int(input())
for i in range(a):
    z = []
    lol.append(input())
gor = horizontal_reflection(lol)
ver = vertical_reflection(lol)
trans = transpose(lol)
gorver = horizontal_reflection(lol)      
gorver = vertical_reflection(gorver)
gortrans = horizontal_reflection(lol)
gortrans = transpose(gortrans)
verttrans = vertical_reflection(lol)
verttrans = transpose(verttrans)
transgorver = transpose(lol)   # несколько отражений выполняем с помощью выполнения функций поочереди
transgorver = horizontal_reflection(transgorver)
transgorver = vertical_reflection(transgorver)
for i in range(a):
    print(lol[i])
print()
for i in range(a):
    print(''.join(gor[i]))
print()
for i in range(a):
    print(ver[i])
print()
for i in range(a):
    print(''.join(trans[i]))
print()
for i in range(a):
    print(''.join(gorver[i]))
print()
for i in range(a):
    print(''.join(gortrans[i]))
print()
for i in range(a):
    print(''.join(verttrans[i]))
print()
for i in range(a):
    print(''.join(transgorver[i]))