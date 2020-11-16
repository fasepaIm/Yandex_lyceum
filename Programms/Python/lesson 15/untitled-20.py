a = input().split()
b = []
for i in a:
    if i[-1].isdigit():
        b.append(i)
    else:
        if i == '+':
            c = int(b[-2]) + int(b[-1])
            b.pop(-2)
            b.pop(-1)
            b.append(c)
        elif i == '-':
            c = int(b[-2]) - int(b[-1])
            b.pop(-2)
            b.pop(-1)
            b.append(c)
        elif i == '*':
            c = int(b[-2]) * int(b[-1])
            b.pop(-2)
            b.pop(-1)
            b.append(c)
        elif i == '#':
            c = b[-1]
            b.pop(-1)
            b.append(c)
            b.append(c)
        elif i == '!':
            c = 1
            for i in range(1, int(b[-1]) + 1):
                c *= i
            b.pop(-1)
            b.append(c)
        elif i == '/':
            c = int(b[-2]) // int(b[-1])
            b.pop(-2)
            b.pop(-1)
            b.append(c)
        elif i == '@':
            b[-1], b[-2] = b[-2], b[-1]
            b[-1], b[-3] = b[-3], b[-1]
        elif i == '~':
            c = int(b[-1]) * -1
            b.pop(-1)
            b.append(c)
print(str(b)[1:-1])