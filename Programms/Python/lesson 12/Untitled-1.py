cnt = int(input())
lol = 1
hehe = []
spiska = []
x = ''
while lol not in hehe:
    hehe.append(lol)
    spiska.append((10 * lol) // cnt)
    lol = (10 * lol) % cnt
spiska = spiska[hehe.index(lol):]
for i in spiska:
    x += str(i)
print(x)