a, z = [5], [5] #  списки - это изменяемые объекты, а строки - неизменяемые
c, d = 6, 6


def plus_rav(a): # вызываем список и изменяем его
    a += [4]


plus_rav(a)
print(a)


def rav_plus(z): # 
    z = z + [4]


rav_plus(z)
print(z)


def rav1(c):
    c += 4


rav1(c)
print(c)


def rav2(d):
    d = d + 4


rav2(d)
print(d)