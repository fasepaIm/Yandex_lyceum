a = [' *   ', '* *  ', '***  ', '* *  ', '* *  ']
b = ['**   ', '* *  ', '**   ', '* *  ', '**   ']
c = [' *   ', '* *  ', '*    ', '* *  ', ' *   ']
f = ['', '', '', '', '']
d = input()
for j in range(5):
    for i in range(len(d)):
        if d[i] == 'A':
            f[j] += a[j]
        if d[i] == 'B':
            f[j] += b[j]
        if d[i] == 'C':
            f[j] += c[j]
for i in f:
    print(i)