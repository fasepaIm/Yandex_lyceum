lol = {}
a = input().split()
for i in a:
    if i not in lol:
        lol[i] = 1
    else:
        lol[i] += 1
    print(lol[i], end=' ')