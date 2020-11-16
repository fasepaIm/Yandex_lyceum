a = int(input())
mojno = []
hehe = []
lol = []
for i in range(a):
    z = ''
    b = input().split('/')
    b = b[1:]
    mojno.append(b)
    lol.append(b[0])
c = int(input())
for i in range(c):
    z = ''
    b = input().split('/')
    b = b[1:]
    hehe.append(b)
for i in hehe:
    x = 0
    f = 0
    if i[0] not in lol:
        print('NO')
        continue
    for j in mojno:
        for k in range(len(i)):
            if k < len(j):
                if i[k] == j[k]:
                    x += 1
                if x == len(j):
                    break
        if x == len(j):
            print('YES')
            f = 1
            break
        x = 0
    if f == 0:
        print('NO')
        f = 0