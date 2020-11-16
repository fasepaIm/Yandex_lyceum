lol = int(input())
z = [0] * lol
for i in range(lol):
    z[i] = ['-'] * lol
for i in range(1, lol):
    x = input().split()
    for j in range(len(x)):
        z[i][j] = int(x[j])
for i in range(lol - 1):
    for j in range(lol):
        if z[i][::-1][j] == '-':
            z[i][lol - j - 1] = z[lol - i - 1][j]
xx, yy = input().split()
xx = int(xx)
yy = int(yy)
pip = xx
if xx > yy:
    xx, yy = yy, xx
vv = z[yy][xx]
for i in range(lol):
    if i != xx and i != yy and z[i][xx] != '-' and z[i][yy] != '-':
        if z[i][yy] + z[i][xx] < vv:
            vv = z[i][yy] + z[i][xx]
            pip = i
print(pip)