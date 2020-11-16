a, b, c, d = int(input()), int(input()), input(), int(input())
if c == 'луна':
    b += d
if c == 'солнце':
    a += d
if a > b:
    print('солнечное')
else:
    print('лунное')