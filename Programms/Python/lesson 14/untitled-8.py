a = input()
b = []
while a != '':
    b.append(a)
    a = input()
passwords = [i for i in input().split(';')]
for i in b:
    c = [j for j in i.split(':')]
    if c[1] in passwords:
        print('To:', c[0])
        d = ' '.join([i for i in c[4].split(',')][:1])
        print(d + ', ваш пароль слишком простой, смените его.')