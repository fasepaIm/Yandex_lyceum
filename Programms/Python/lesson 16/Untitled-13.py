a = int(input())
lol = []
name = input()
hodi = int(input())
for i in range(hodi):
    if name == 'Петя':
        while a % 2 == 0:
            a = a // 2
        while a % 3 == 0:
            a = a // 3
        a += 11
        lol.append(a)
        name = 'Маша'
    elif name == 'Маша':
        a = a * 3 - 2
        lol.append(a)
        name = 'Петя'
lol.sort()
if len(lol) % 2 != 0:
    print(lol[len(lol) // 2])
else:
    print((lol[len(lol) // 2 - 1] + lol[len(lol) // 2]) / 2)