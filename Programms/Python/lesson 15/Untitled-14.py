a = input().split()
b = []
for i in a:
    if i[-1].isdigit():
        b.append(i)
    else:
        if i == '+':
            c = int(b[-2]) + int(b[-1])
        elif i == '-':
            c = int(b[-2]) - int(b[-1])
        elif i == '*':
            c = int(b[-2]) * int(b[-1])
        b.pop(-2)
        b.pop(-1)
        b.append(c)
print(str(b)[1:-1])