a = input()
b = 0
c = [0] * 30000
m = 0
for i in a:
    if i == '[':
        m += 1
        if c[b] == 0:
            continue
        else:
            f = b
            s = a[a.find('[') + 1:a.find(']')]
            while c[f] != 0:
                for j in s:
                    if j == '>':
                        b = (b + 1) % 30000
                    if j == '<':
                        b = (b - 1) % 30000
                    if j == '+':
                        c[b] = (c[b] + 1) % 256
                    if j == '-':
                        c[b] = (c[b] - 1) % 256
                    if j == '.':
                        print(c[b])
    if i == ']' and m == 1:
        m -= 1
        continue
    if m == 0:
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