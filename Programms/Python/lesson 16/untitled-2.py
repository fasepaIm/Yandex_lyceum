a = input()
b = 0
c = [0] * 30000
for i in a:
    if i == '>':
        b = (b + 1) % 30000
    if i == '<':
        b = (b - 1) % 30000
    if i == '+':
        c[b] = (c[b] + 1) % 256
    if i == '-':
        c[b] = (c[b] - 1) % 256
    if i == '.':
        print(c[b])